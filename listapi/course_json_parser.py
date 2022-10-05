import json

from models import *


class CourseJSONObjectParser:
    def __init__(self, json_object):
        self.json_object = json_object

    def get_instructor(self):
        instructor_array = self.json_object["instructors"]
        first_instructor_json = instructor_array[0]
        name = first_instructor_json["name"]
        email = first_instructor_json["email"]
        return Instructor(name=name, email=email)

