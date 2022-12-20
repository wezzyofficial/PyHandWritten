![PyHandWritten preview](https://raw.githubusercontent.com/wezzyofficial/PyHandWritten/master/assets/screen1.jpg)

# PyHandWritten

#### _Ваши конспекты в тетрадь - меньше чем за 10 сек._
PyHandWritten работает на [Flask 2.2+](https://flask.palletsprojects.com/en/2.2.x/) / [SqlAlchemy 1.4+](https://www.sqlalchemy.org/) / [Jinja2 3.1+](https://jinja.palletsprojects.com/en/3.1.x/) и [Pillow 9.3+](https://pillow.readthedocs.io/en/stable/).


## Установка
Для начала установите зависимости для запуска проекта:

```sh
pip install requirements.txt
```

> Измените подключение к базе данных в engine/settings.py, если планируете использовать другую базу - [тык](https://docs.sqlalchemy.org/en/14/core/engines.html).
> Если же нет, то можем просто запустить базу данных в Docker, через docker-compose.

Для запуска базы данных в Docker, через docker-compose:
```sh
docker-compose up -d
```

Далее нам необходимо провести применить миграции базы данных:

```sh
Автоматическое создания моделей > alembic revision --autogenerate -m "migrate all models"
Применения изменений > alembic upgrade head
```

Ну и запускаем на проект:
```sh
python main.py
```

> Перед развертываем проекта в prod, не забываем выключить DEBUG мод в настройках проекта.