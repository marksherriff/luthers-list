import json
import os
from listapi.course_json_parser import CourseJsonParser


def get_all_json_files():
    pass
    ## loop through all json files
    ## or get the json for each subject somehow

    ## call load_json_file (filename) if it's a file
    ## or call load_json_string if string
    ## or call load_json_array if array


def load_json_file(filename):
    json_file = open(filename, 'r')
    json_string = json_file.read()
    load_json_string(json_string)


def load_json_string(json_string):
    json_array = json.loads(json_string)
    load_json_array(json_array)


def load_json_array(json_array):
    for json_object in json_array:
        load_database_from_json_object(json_object)


def load_database_from_json_object(json_object):
    cpj = CourseJsonParser(json_object)
    cpj.load_all()
