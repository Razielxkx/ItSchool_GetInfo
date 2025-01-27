from src.db import Base
from sqlalchemy import Column, Integer, String


class Courses(Base):
    __tablename__ = "courses"
    index = Column(Integer, primary_key=True)
    title = Column(String(50))
    type = Column(String(50))

    def __repr__(self):
        return f"Id:{self.index}\nTitle:{self.title}\nType:{self.type}\n"


class Trainers(Base):
    __tablename__ = "trainers"
    index = Column(Integer, primary_key=True)
    name = Column(String(50))
    specialization = Column(String(100))
    description = Column(String(10000))

    def __repr__(self):
        return f"Id:{self.index}\nName:{self.name}\nSpecialization:{self.specialization}\nDescription:{self.description}\n"
