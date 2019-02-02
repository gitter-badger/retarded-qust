import requests
from bs4 import BeautifulSoup
import execjs


username = ""
password = ""

s = requests.Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "\
                          "AppleWebKit/537.36 (KHTML, like Gecko) "\
                          "Chrome/73.0.3683.10 Safari/537.36"

login_page = s.get("http://ipass.qust.edu.cn/tpass/login")
soup = BeautifulSoup(login_page.content, 'html.parser')
exec_ctx = execjs.compile(open("des.js", "r").read())

lt = soup.find_all("input", id="lt")[0]["value"]
login_page = s.post("http://ipass.qust.edu.cn/tpass/login", data={
    "rsa": exec_ctx.call("strEnc", username + password + lt, "1", "2", "3"),
    "ul": len(username),
    "pl": len(password),
    "lt": lt,
    "execution": soup.find_all("input", {'name': "execution"})[0]["value"],
    "_eventId": soup.find_all("input", {'name': "_eventId"})[0]["value"]
})
with open("test.html", "wb") as file:
    file.write(login_page.content)
