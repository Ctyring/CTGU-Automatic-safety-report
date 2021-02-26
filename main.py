import requests
from lxml import etree
import os
session = requests.session()
url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
files = {'upload': open('test.txt', 'rb')}
username = '2020112805'
password = os.environ['password']
ip = os.environ['ip']
data = {
    'username': username,
    'password': password,
}
proxies = {
    'http':ip,
    'https':ip,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Referer': 'http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019&showWjdc=false&studentShowWjdc=false',
}
response = session.post(url = url,params=data,files=files,headers = headers,proxies = proxies)
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Referer': 'http://yiqing.ctgu.edu.cn/wx/health/main.do',
}
res = session.get('http://yiqing.ctgu.edu.cn/wx/health/toApply.do',headers = headers2,proxies=proxies).text
tree = etree.HTML(res)
token = tree.xpath('/html/body/main/section/form/input[1]/@value')
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Referer': 'http://yiqing.ctgu.edu.cn/wx/health/toApply.do',
}
data2 = {
    'ttoken': token,
    'province':'湖北省',
    'city':'宜昌市',
    'district':'西陵区',
    'adcode':'443000',
    'longitude':'111',
    'latitude':'31',
    'sfqz':'否',
    'sfys':'否',
    'sfzy':'否',
    'sfgl':'否',
    'status':'1',
    'szdz':'湖北省 宜昌市 西陵区',
    'sjh':'15385206196',
    'lxrxm':'',
    'lxrsjh':'',
    'sffr':'否',
    'sffrAm':'否',
    'sffrNoon':'否',
    'sffrPm':'否',
    'sffy':'否',
    'sfgr':'否',
    'qzglsj':'',
    'qzgldd':'',
    'glyy':'',
    'mqzz':'',
    'sffx':	'否',
    'qt':'',
}
res2 = session.post('http://yiqing.ctgu.edu.cn/wx/health/saveApply.do',headers = headers3,data = data2,proxies=proxies)
print(res2)
