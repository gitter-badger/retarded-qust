import point
import login
import course
import argparse
import getpass


def print_score():
    """print all of your score"""

    unformatted_header = "{:16s}|{:6s}|{:6s}|{:6s}|{:12s}|{:18s}|{:24s}"
    unformatted_body = "{:16s}|{:6.1f}|{:6.1f}|{:6.1f}|{:12s}|{:18s}|{:24s}"

    print(unformatted_header.
          format('Course ID', 'Grade', 'Point', 'Credit', 'School year', 'Date of completion', "Course Name"))
    print(unformatted_header.
          format("-" * 16, "-" * 6, "-" * 6, "-" * 6, "-" * 12, "-" * 18, "-" * 24))
    for single in all_point:
        print(unformatted_body.format(
            single['courseID'],
            single['grade'],
            single['point'],
            single['credit'],
            single['schoolYear'],
            single['completionDate'],
            single['courseName']))


def print_help():
    """print this help message"""
    print("you can enter the following command to operate:")
    for k, v in command_action_dict.items():
        print("\t{:10s}{}".format(k, v.__doc__))


def exit_it():
    """exit the program"""
    exit()


command_action_dict = {"help": print_help, "score": print_score, "exit": exit_it}


all_point = dict()


def main():
    parser = argparse.ArgumentParser(
        description='Retarded QUST, aka 智障青科大, facilitate the destruction of the university for students')

    username_help = "input the username of i.qust.edu.cn, aka your student ID"
    password_help = "input the password of i.qust.edu.cn, the default one is the last six digits of your ID card"
    parser.add_argument('-u', '--username', help=username_help)
    parser.add_argument('-p', '--password', help=password_help)

    args = parser.parse_args()
    if not args.username:
        args.username = input(username_help + "\n>> username: ")
    if not args.password:
        args.password = getpass.getpass(password_help + "\n>> password: ")
    course_dict = course.build_course_dict()

    global all_point
    all_point = course.add_course_name_to_result(point.get_point(login.login(args.username, args.password)), course_dict)

    print("input query commands, 'help' for help.")
    while True:
        command = input(">> ")
        command_action_dict[command]()


main()
