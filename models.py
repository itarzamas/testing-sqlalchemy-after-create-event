# models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Unicode
from sqlalchemy.orm import relationship

Base = declarative_base()


class Todo (Base):
    __tablename__ = "todo"
    id = Column('id', Integer, primary_key = True)
    priority_id = Column('priority_id', Integer, ForeignKey('priority.id'))
    title = Column('title', Unicode)
    description = Column('description', Unicode)

    priority = relationship('Priority', foreign_keys=priority_id)


class Priority (Base):
    __tablename__ = "priority"
    id = Column('id', Integer, primary_key = True)
    name = Column('name', Unicode)


