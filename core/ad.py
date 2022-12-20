from flask import render_template


def route_error(text: str = '404: Страница не найдена!') -> str:
    return render_template('error.html', text_error=text)