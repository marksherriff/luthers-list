from .models import *


class CourseJsonParser:
    def __init__(self, json_object):
        self.json_object = json_object

    def get_instructor(self):
        instructor_array = self.json_object["instructors"]
        first_instructor_json = instructor_array[0]
        name = first_instructor_json["name"]
        email = first_instructor_json["email"]
        return Instructor(name=name, email=email)

    def get_section(self):
        ray = Instructor.objects.get(email="rp6zr@virginia.edu")
        return Section(instructor=ray,
                       course_section=self.json_object["class_section"],
                       subject=self.json_object["subject"],
                       # course_id=int(self.json_object["crse_id"]),
                       semester_code=int(self.json_object["strm"]))
