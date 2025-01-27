import pandas as pd
from src.db import engine, SessionLocal
from src.tables import Trainers, Courses
from src.scrapper import ItSchoolScrapper


class ItSchoolDb:
    @staticmethod
    def _generate_trainers():
        trainers_scrapper = ItSchoolScrapper("despre/traineri")
        trainers = trainers_scrapper.get_trainers()
        trainers_df = pd.DataFrame.from_dict(trainers, orient="index")
        trainers_df.to_sql("trainers", engine, if_exists="replace", index=True)

    @staticmethod
    def _generate_courses():
        courses_scrapper = ItSchoolScrapper("cursuri")
        courses = courses_scrapper.get_courses()
        df = pd.DataFrame.from_dict(courses, orient="index")
        df.to_sql("courses", engine, if_exists="replace", index=True)

    @staticmethod
    def get_all_trainers():
        with SessionLocal() as session:
            trainers = session.query(Trainers).all()
            if trainers:
                return trainers
            ItSchoolDb._generate_trainers()
            return session.query(Trainers).all()

    @staticmethod
    def get_trainer(name):
        with SessionLocal() as session:
            return session.query(Trainers).filter(Trainers.name == name).first()


    @staticmethod
    def get_all_courses():
        with SessionLocal() as session:
            courses = session.query(Courses).all()
            if courses:
                return courses
            ItSchoolDb._generate_courses()
            return session.query(Courses).all()

    @staticmethod
    def get_course(title):
        with SessionLocal() as session:
            return session.query(Courses).filter(Courses.title == title).first()
