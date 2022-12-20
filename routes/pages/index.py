from core import handler
from flask import render_template


@handler.route(name='', get=True)
def _(request, db, url_path, path_args, payloads):
    return render_template('index.html')