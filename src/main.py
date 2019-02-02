import point
import login

if __name__ == '__main__':
    all_point = point.get_point(login.login('', ''))
    for single in (all_point['list']):
        print('课程号:' + single['KCH'], \
              '成绩:' + str(single['KCCJ']), \
              '绩点:' + str(single['JD']), \
              '学分:' + str(single['XF']), \
              '学年:' + str(single['XN']), \
              '成绩填写日期:' + single['CJLRRQ'])
