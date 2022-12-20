import platform
from core import handler
from core.ad import route_error
from core.draw.ttp import TextToPicture
from engine.models import Turns, ProcessedText


@handler.route(name='processing', post=True)
def _(request, db, url_path, path_args, payloads):
    st, data, args = None, payloads['data'], payloads['args']
    if data is not None:
        st = data.get('source_text')

    if args is not None:
        st = args.get('source_text')

    if st is not None:
        count_st = len(st.replace('\n', ''))
        if count_st > 0 and count_st <= 4096:
            turn_data = Turns(st=st)
            db.add(turn_data)
            db.commit()

            ttt = TextToPicture(text=turn_data.st, hash_d=turn_data.hash)
            pt = ttt.word_processing()

            ri_html = ""
            for n, p in enumerate(pt, start=1):
                fn = p.split('/')[-1]
                if platform.system() == 'Windows':
                    fn = p.split('\\')[-1]

                proc_t = ProcessedText(turn=turn_data, file_name=fn, file_path=p)
                db.add(proc_t)
                db.commit()

                ri_html += f'''
                \n
                <div class="ri">
                    <p class="ri-name">#{n}</p>
                    <a href="/download?hash={turn_data.hash}&id={proc_t.id}" target="_blank">
                      <img src="/static/download.png">
                    </a>
                </div>
                \n
                '''

            ri_html += '''
                <a class="ri-button" href="/">ПРЕОБРАЗОВАТЬ ЕЩЕ РАЗ</a>
            '''

            return {
                'status': True,
                'hash': turn_data.hash,
                'html': ri_html
            }
        else:
            html = f'''
                <p class="text-error">Разрешено кол-во символов < {count_st}/4096!</p>
                <a class="ri-button" href="/">ВЕРНУТЬСЯ НА ГЛАВНУЮ</a>
            '''

            return {
                'status': False,
                'html': html
            }
    else:
        return route_error(text='В запросе отсутсвует полезная нагрузка!')