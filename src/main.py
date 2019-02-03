import point
import login
import argparse

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
    args.password = input(password_help + "\n>> password: ")
all_point = point.get_point(login.login(args.username, args.password))

unformatted_header = "{:24s}|{:6s}|{:6s}|{:6s}|{:12s}|{:18s}"
unformatted_body = "{:24s}|{:6.1f}|{:6.1f}|{:6.1f}|{:12s}|{:18s}"

print(unformatted_header.
      format('Course ID', 'Grade', 'Point', 'Credit', 'School year', 'Date of completion'))
print(unformatted_header.
      format("-" * 24, "-" * 6, "-" * 6, "-" * 6, "-" * 12, "-" * 18))
for single in all_point['list']:
    print(unformatted_body.
          format(single['KCH'], single['KCCJ'], single['JD'], single['XF'], single['XN'], single['CJLRRQ']))
