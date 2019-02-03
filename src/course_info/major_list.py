import requests
import json

url = "http://jwglxt.qust.edu.cn/jwglxt/jxzxjhgl/jxzxjhck_cxJxzxjhckIndex.html"

querystring = {"doType":"query","gnmkdm":"N153540","su":"1608080103"}

payload = "jg_id=&njdm_id=2016&dlbs=&zyh_id=&_search=false&nd=1549173611399&queryModel.showCount=15000&queryModel.currentPage=1&queryModel.sortName=&queryModel.sortOrder=asc&time=5"
headers = {
    'Host': "jwglxt.qust.edu.cn",
    'Connection': "keep-alive",
    'Content-Length': "166",
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

ans_json = (response.json())

all_course = (ans_json['items'])

text = ""

for single in all_course:
    course_id = single['jxzxjhxx_id']
    course_name = single['zymc']
    course_place = single['xqmc']
    print(single['jxzxjhxx_id'],single['zymc'],single['xqmc'])
    text += course_id
    text += '\n'

with open('course_number.txt','w') as file:
    file.write(text)