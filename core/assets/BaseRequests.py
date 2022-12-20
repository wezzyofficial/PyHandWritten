import traceback, sys
from core.ad import route_error


class Route:
    def __init__(self, **kwargs):
        if not kwargs.keys() & {'name', 'handler', 'admin'}:
            raise Exception('Not enough arguments to create command object')
        self.name = [n.lower() for n in kwargs['name']] if type(kwargs['name']) == list else kwargs['name'].lower()
        self.__handler = kwargs['handler']
        self.post = kwargs['post']
        self.get = kwargs['get']
        self.put = kwargs['put']
        self.with_args = kwargs['with_args']


    def handle(self, r, db, up, pa, p):
        try:
            # if self.auth and token_verif is False:
            #     return {
            #         'status': False,
            #         'message': 'Wrong authorization token!'
            #     }

            if self.post and r.method == 'POST' == False:
                return {
                    'status': False,
                    'message': 'Wrong request method - need POST!'
                }

            if self.get and r.method == 'GET' == False:
                return {
                    'status': False,
                    'message': 'Wrong request method - need GET!'
                }

            if self.put and r.method == 'PUT' == False:
                return {
                    'status': False,
                    'message': 'Wrong request method - need PUT!'
                }

            return self.__handler(request=r, db=db, url_path=up, path_args=pa, payloads=p)
        except Exception:
            ex_type, ex, tb = sys.exc_info()
            print(ex, traceback.format_tb(tb))
            return route_error(text='500: Произошла ошибка сервера!')