import json


def build_course_dict():
    course_dict = dict()
    with open("src/course_info/course_all_info.txt", "r", encoding="GBK") as info_file:
        for line in info_file.readlines():
            line_json = json.loads(line.replace("'", '"'))
            course_dict[line_json['kch']] = line_json['kcmc']
    return course_dict


def add_course_name_to_result(result, course_dict):
    for i in result:
        course_name = course_dict.get(i['courseID'])
        if not course_name:
            course_name = "unknown"
        i['courseName'] = course_name
    return result
