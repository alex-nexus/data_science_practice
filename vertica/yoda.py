from sqlalchemy import Column, Integer, Unicode, Unicode, Text, DateTime, Sequence, Boolean, Date, UnicodeText, UniqueConstraint, Table, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, column_property, relationship, backref
import numpy as NP
import codecs

#models
class Yoda(Base):
    __tablename__ = 'yoda'
    action_name = Column(String)
    action_type = Column(String)
    action_time = Column(String)
    method = Column(String)

