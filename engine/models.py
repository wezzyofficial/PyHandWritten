from sqlalchemy.sql import func
from core.af.generate import new_hex
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey


Base = declarative_base()


class Model(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Turns(Model):
    __tablename__ = "turns"

    hash = Column(Text, default=new_hex, nullable=False)
    st = Column(Text, default='', nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Turns {self.id} {self.hash} {self.complete}>"


class ProcessedText(Model):
    __tablename__ = "proccesed_text"

    turn_id = Column(Integer, ForeignKey('turns.id'))
    turn = relationship("Turns")

    file_name = Column(Text, default='', nullable=True)
    file_path = Column(Text, default='', nullable=True)

    def __repr__(self):
        return f'<PT {self.id} {self.turn.id} {self.file_path}>'