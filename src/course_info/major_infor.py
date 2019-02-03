import requests,json,re


with open('course_number.txt','r') as file:
    number = file.read()
number_list = number.split('\n')

for single_number in number_list:
    print(single_number)
    url = "http://jwglxt.qust.edu.cn/jwglxt/jxzxjhgl/jxzxjhkcxx_cxJxzxjhkcxxIndex.html"

    querystring = {"doType":"query","gnmkdm":"N153540","su":"1608080103"}

    payload = "jyxdxnm=&jyxdxqm=&yxxdxnm=&yxxdxqm=&shzt=&kch=&jxzxjhxx_id="+single_number+"&xdlx=&_search=false&nd=1549172767053&queryModel.showCount=99999999&queryModel.currentPage=1&queryModel.sortName=jyxdxnm%2Cjyxdxqm%2Ckch&queryModel.sortOrder=asc&time=9"
    headers = {
        'Host': "jwglxt.qust.edu.cn",
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "http://jwglxt.qust.edu.cn",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded;charset=UTF-8",
        'Referer': "http://jwglxt.qust.edu.cn/jwglxt/jxzxjhgl/jxzxjhck_cxJxzxjhckIndex.html?gnmkdm=N153540&layout=default&su=1608080103",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "JSESSIONID=D30C1D6F44789F9F3BB5B794F66FC587",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    ans_json = (response.json()['items'])

    for single_json in ans_json:
        with open('course_all_infor.txt','a') as file:
            # single_json = re.sub('yyxdxnxqmc','course_year',single_json)
            # single_json = re.sub('xsxxxx', 'course_type', single_json)
            # single_json = re.sub('xf', 'course_point', single_json)
            # single_json = re.sub('jxzxjhkcxx_id', 'course_number', single_json)
            # single_json = re.sub('kcmc', 'course_name', single_json)
            # single_json = re.sub('kkbmmc', 'course_institute', single_json)
            print(single_json)
            file.write(str(single_json)+'\n')

