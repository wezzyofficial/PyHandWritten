from pathlib import Path
from core import handler
from core.ad import route_error
from flask import Flask, request
from core.database import session
from core.loaders import read_handlers


class WebServer:
    def __init__(self):
        self.__project_path = f'{Path(__file__).parents[1]}'
        self.app = Flask(__name__, root_path=self.__project_path, template_folder='templates', static_folder='static')
        self.db = session

        read_handlers()
        self.create_listeners()

        self.app.run(debug=False)


    def extract_payload(self, request):
        payloads = {
            'data': None,
            'args': None
        }

        if len(request.form) > 0:
            payloads['data'] = {}
            for key in request.form:
                payloads['data'][key] = request.form[key]

        if len(request.args) > 0:
            payloads['args'] = {}
            for key in request.args:
                payloads['args'][key] = request.args[key]

        return payloads


    def extract_host_path_args(self, request, url_path: str):
        rhu = f'{request.host_url}/{url_path}'

        host_url = rhu.replace('http://', '')
        host_url = host_url.replace('https://', '')
        host_url = host_url.replace(f'{request.host}/', '')
        host_url = host_url.replace(f'{request.host}//', '')
        host_url = host_url.replace(request.host, '')

        path_args = host_url.split('/')

        for n, pa in enumerate(path_args):
            if pa == '':
                path_args.pop(n)

        return host_url, path_args


    def check_route(self, route, path_args, routes_list, url_path) -> bool:
        route_correct = False
        if route.with_args:
            pa = ''
            if len(path_args) > 0:
                pa = path_args[0]

            if pa in routes_list:
                route_correct = True
        else:
            if url_path in routes_list:
                route_correct = True

        return route_correct


    def create_listeners(self):
        def processing_route(request, url_path):
            host_url, path_args = self.extract_host_path_args(request=request, url_path=url_path)
            payloads = self.extract_payload(request=request)

            for route in handler.routes:
                routes_list = [route.name]
                if type(route.name) == list:
                    routes_list = [r for r in route.name]

                route_correct = self.check_route(route=route, path_args=path_args, routes_list=routes_list,
                                                 url_path=url_path)

                if route_correct:
                    return route.handle(r=request, db=self.db, up=url_path, pa=path_args, p=payloads)

            else:
                return route_error()


        @self.app.route('/<path:path>', methods=['GET', 'POST'])
        def routes_handler(path):
            return processing_route(request=request, url_path=path)


        @self.app.route('/', methods=['GET', 'POST'])
        def routes_handler_index():
            return processing_route(request=request, url_path='')

        @self.app.teardown_appcontext
        def shutdown_session(exception=None):
            self.db.close()