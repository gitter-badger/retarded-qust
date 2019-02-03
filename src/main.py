import point
import login
import course
import query_expression
import argparse
import getpass


def print_score(args):
    """print score by your input condition, for example: `where AND(schoolYear == "2018-2019", grade < 60)`,
            you can use `courseID`, `grade`, `point`, `credit`, `schoolYear`, `completionDate` and `courseName` in the expression"""

    query_obj = None
    if args:
        query_obj = query_expression.generate_query(args)

    unformatted_header = "{:16s}|{:6s}|{:6s}|{:6s}|{:12s}|{:18s}|{:24s}"
    unformatted_body = "{:16s}|{:6.1f}|{:6.1f}|{:6.1f}|{:12s}|{:18s}|{:24s}"

    print(unformatted_header.
          format('Course ID', 'Grade', 'Point', 'Credit', 'School year', 'Date of completion', "Course Name"))
    print(unformatted_header.
          format("-" * 16, "-" * 6, "-" * 6, "-" * 6, "-" * 12, "-" * 18, "-" * 24))
    for single in all_point:
        if (query_obj and query_obj.eval(single)) or not query_obj:
            print(unformatted_body.format(
                single['courseID'],
                single['grade'],
                single['point'],
                single['credit'],
                single['schoolYear'],
                single['completionDate'],
                single['courseName']))


def print_all_score(args):
    """print all of your score"""

    print_score("")


def print_help(args):
    """print this help message"""
    print("you can enter the following command to operate:")
    for k, v in command_action_dict.items():
        print("\t{:10s}{}".format(k, v.__doc__))


def exit_it(args):
    """exit the program"""
    exit()


command_action_dict = {
    "help": print_help,
    "all": print_all_score,
    "where": print_score,
    "exit": exit_it
}


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
        command = input(">> ").split(maxsplit=1)
        command_name = command[0]
        command_args = None
        if len(command) > 1:
            command_args = command[1]
        func = command_action_dict.get(command_name)
        if not func:
            print("command not found")
        else:
            func(command_args)


main()
