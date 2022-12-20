from engine.settings import DATABASE

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


db_engine = create_engine(URL(**DATABASE))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))

session = db_session()