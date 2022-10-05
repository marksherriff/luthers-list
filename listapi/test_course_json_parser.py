import json

from django.test import TestCase

from .models import *
from .course_json_parser import CourseJsonParser


def cs1110_001_json_string():
    return """
    {
        "index": 2,
        "crse_id": "006846",
        "crse_offer_nbr": 1,
        "strm": "1228",
        "session_code": "SRT",
        "session_descr": "Short Add",
        "class_section": "001",
        "location": "MAIN",
        "location_descr": "On Grounds",
        "start_dt": "08/23/2022",
        "end_dt": "12/06/2022",
        "class_stat": "A",
        "campus": "MAIN",
        "campus_descr": "Main Campus",
        "class_nbr": 16003,
        "acad_career": "UGRD",
        "acad_career_descr": "Undergraduate",
        "component": "LEC",
        "subject": "CS",
        "subject_descr": "Computer Science",
        "catalog_nbr": "1110",
        "class_type": "E",
        "schedule_print": "Y",
        "acad_group": "ENGR",
        "instruction_mode": "P",
        "instruction_mode_descr": "In Person",
        "acad_org": "CS",
        "wait_tot": 0,
        "wait_cap": 199,
        "class_capacity": 275,
        "enrollment_total": 274,
        "enrollment_available": 1,
        "descr": "Introduction to Programming",
        "rqmnt_designtn": "",
        "units": "3",
        "combined_section": "N",
        "enrl_stat": "O",
        "enrl_stat_descr": "Open",
        "topic": "",
        "instructors": [
          {
            "name": "Raymond Pettit",
            "email": "rp6zr@virginia.edu"
          }
        ],
        "section_type": "Lecture",
        "meetings": [
          {
            "days": "MoWeFr",
            "start_time": "14.00.00.000000-05:00",
            "end_time": "14.50.00.000000-05:00",
            "start_dt": "08/23/2022",
            "end_dt": "12/06/2022",
            "bldg_cd": "WNR",
            "bldg_has_coordinates": false,
            "facility_descr": "John W. Warner Hall 209",
            "room": "209",
            "facility_id": "WNR 209",
            "instructor": "Raymond Pettit"
          }
        ],
        "crse_attr": "NCLC",
        "crse_attr_value": "NCLC-NOCOST",
        "reserve_caps": []
    }"""


def cs3240_002_json_string():
    return """
    {
    "index": 48,
    "crse_id": "006903",
    "crse_offer_nbr": 1,
    "strm": "1228",
    "session_code": "SRT",
    "session_descr": "Short Add",
    "class_section": "001",
    "location": "MAIN",
    "location_descr": "On Grounds",
    "start_dt": "08/23/2022",
    "end_dt": "12/06/2022",
    "class_stat": "A",
    "campus": "MAIN",
    "campus_descr": "Main Campus",
    "class_nbr": 15991,
    "acad_career": "UGRD",
    "acad_career_descr": "Undergraduate",
    "component": "LEC",
    "subject": "CS",
    "subject_descr": "Computer Science",
    "catalog_nbr": "3240",
    "class_type": "E",
    "schedule_print": "Y",
    "acad_group": "ENGR",
    "instruction_mode": "P",
    "instruction_mode_descr": "In Person",
    "acad_org": "CS",
    "wait_tot": 0,
    "wait_cap": 199,
    "class_capacity": 135,
    "enrollment_total": 134,
    "enrollment_available": 1,
    "descr": "Advanced Software Development Techniques",
    "rqmnt_designtn": "",
    "units": "3",
    "combined_section": "N",
    "enrl_stat": "C",
    "enrl_stat_descr": "Closed",
    "topic": "",
    "instructors": [
      {
        "name": "Paul McBurney",
        "email": "pm8fc@virginia.edu"
      },
      {
        "name": "Mark Sherriff",
        "email": "mss2x@virginia.edu"
      }
    ],
    "section_type": "Lecture",
    "meetings": [
      {
        "days": "TuTh",
        "start_time": "15.30.00.000000-05:00",
        "end_time": "16.45.00.000000-05:00",
        "start_dt": "08/23/2022",
        "end_dt": "12/06/2022",
        "bldg_cd": "RICE",
        "bldg_has_coordinates": true,
        "facility_descr": "Rice Hall 130",
        "room": "130",
        "facility_id": "RICE 130",
        "instructor": "Paul McBurney"
      }
    ],
    "crse_attr": "",
    "crse_attr_value": "",
    "reserve_caps": []
  }
    """


class CourseJsonParserTest(TestCase):

    def test_get_instructor_one_instructor(self):
        cs1110 = json.loads(cs1110_001_json_string())
        cjp = CourseJsonParser(cs1110)
        ray = cjp.get_instructor()
        self.assertEqual(ray.name, "Raymond Pettit")
        self.assertEqual(ray.email, "rp6zr@virginia.edu")


