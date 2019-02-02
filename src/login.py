import requests
from bs4 import BeautifulSoup
import execjs


def login(username, password):
    s = requests.Session()
    s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "\
                              "AppleWebKit/537.36 (KHTML, like Gecko) "\
                              "Chrome/73.0.3683.10 Safari/537.36"

    login_page = s.get("http://ipass.qust.edu.cn/tpass/login")
    soup = BeautifulSoup(login_page.content, 'html.parser')
    exec_ctx = execjs.compile(open("des.js", "r").read())

    lt = soup.find("input", id="lt")["value"]
    login_res = s.post("http://ipass.qust.edu.cn/tpass/login", data={
        "rsa": exec_ctx.call("strEnc", username + password + lt, "1", "2", "3"),
        "ul": len(username),
        "pl": len(password),
        "lt": lt,
        "execution": soup.find("input", {'name': "execution"})["value"],
        "_eventId": soup.find("input", {'name': "_eventId"})["value"]
    })
    res_soup = BeautifulSoup(login_res.content, 'html.parser')
    user_con = res_soup.find("div", id="user-con")
    if not user_con:
        raise RuntimeError("user not found.")
    print("login as: " + user_con.find("span", {"class": "tit"}).decode_contents())
    return s

