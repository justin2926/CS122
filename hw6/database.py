import sqlalchemy
import sqlite3

from sqlalchemy import create_engine, Column, Float, Integer, String, ForeignKey, Table, Sequence, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.orm import joinedload

engine = create_engine("sqlite:///students.db")

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, Sequence('student_id', start=0, increment=1), primary_key=True)
    name = Column(String)
    major = Column(String)

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, major={self.major})\n"
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

print("Database and tables created successfully")