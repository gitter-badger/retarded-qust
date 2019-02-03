import json


def build_course_dict():
    course_dict = dict()
    with open("src/course_info/course_all_info.txt", "r", encoding="GBK") as info_file:
        for line in info_file.readlines():
            line_json = json.loads(line.replace("'", '"'))
            course_dict[line_json['kch']] = line_json['kcmc']
    return course_dict
