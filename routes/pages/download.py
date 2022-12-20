from core import handler
from flask import send_file
from core.ad import route_error
from engine.models import Turns, ProcessedText


@handler.route(name='download', post=True)
def _(request, db, url_path, path_args, payloads):
    id, hash, data, args = None, None, payloads['data'], payloads['args']
    if data is not None:
        id, hash = data.get('id'), data.get('hash')

    if args is not None:
        id, hash = args.get('id'), args.get('hash')

    if id is not None and hash is not None:
        turns_data = db.query(Turns).filter_by(hash=hash)
        if turns_data.count() > 0:
            turns_data = turns_data.first()
            pt = db.query(ProcessedText).filter_by(turn=turns_data, id=id)
            if pt.count() > 0:
                pt = pt.first()

                return send_file(path_or_file=pt.file_path, download_name=pt.file_name, as_attachment=True)
            else:
                return route_error(text='Эта конвертация не найдена или она уже удалена!')
        else:
            return route_error(text='Эта конвертация не найдена или она уже удалена!')
    else:
        return route_error(text='В запросе отсутсвует полезная нагрузка!')