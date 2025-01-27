import requests
from bs4 import BeautifulSoup


class ItSchoolScrapper:
    def __init__(self, path):
        self.url = f"https://itschool.ro/{path}"
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")

    def _course_details(self):
        details = self.soup.find_all("div", {"class": "CourseCardstyle__Container-sc-1szi4ub-0 eRuMmR"})
        result = {}
        for i, item in enumerate(details):
            title = item.find("h3", {"class": "Typography__H3-sc-wm63nk-2 ePxzQe"})
            course_type = item.find("p", {"class": "Typography__Description-sc-wm63nk-8 euMswu"})
            result[i + 1] = {
                "title": title.text,
                "type": course_type.text
            }
        return result


    def get_courses(self):
        return self._course_details()


    def _trainer_details(self):
        details = self.soup.find_all("div", {"class": "TrainersListstyle__Trainer-sc-1njcztt-3 dBWOha"})
        result = {}
        for i, item in enumerate(details):
            name = item.find("h5", {"class": "Typography__H5-sc-wm63nk-4 ikRFWz"})
            specialization = item.find("p", {"class": "Typography__Body-sc-wm63nk-7 LandingProgramsstyle__Description-sc-1o6bj5c-3 koKZlH cvjzaS"})
            description = item.find("p", {"class": "Typography__Body-sc-wm63nk-7 LandingProgramsstyle__Description-sc-1o6bj5c-3 dXSXuu cvjzaS"})
            result[i + 1] = {
                "name": name.text,
                "specialization": specialization.text,
                "description": description.text
            }
        return result


    def get_trainers(self):
        return self._trainer_details()


if __name__ == "__main__":
    scrapper = ItSchoolScrapper("cursuri")
    courses = scrapper.get_courses()
    print(courses)
