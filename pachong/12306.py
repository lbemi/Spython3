from urllib import request, parse
# from .user import main
import ssl
import http.cookiejar
from json import loads

info = {'user': '934366858@qq.com', 'password': 'Wjl2017'}
c = http.cookiejar.CookieJar()  # 获取请求Cookies
opener = request.build_opener(request.HTTPCookieProcessor(c))  # 构造Cookies请求

ssl._create_default_https_context = ssl._create_stdlib_context  # 使用SSL证书

url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8451187713945497'
# url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=other&rand=sjrand'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}  # 伪造浏览器请求Header
resp = request.Request(url=url, headers=header)  # 构造完整的浏览器请求
html = opener.open(resp).read()  #

with open('yzm.png', 'wb') as f:  # 获取验证码，并保存到本地
    f.write(html)
img = input('验证码：')
# 伪造浏览器Post提交数据

url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}

data = {
    'answer': img,
    'login_site': 'E',
    'rand': 'sjrand'
}  # 构造Post数据
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url=url, headers=header, data=data)
resp = opener.open(req)
html = loads(resp.read())
if html['result_code'] == 4:
    print('验证成功！')
else:

    print('验证失败！')

url = 'https://kyfw.12306.cn/passport/web/login'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
data = {
    'username': info['user'],
    'password': info['password'],
    'appid': 'otn'
}

data = parse.urlencode(data).encode('utf-8')
rep = request.Request(url=url, headers=header, data=data)
html = opener.open(rep).read().decode('utf-8')

# url = 'https://kyfw.12306.cn/otn/leftTicket/init'
# data = {
#     'leftTicketDTO.train_date':'2017-11-29',
#     'leftTicketDTO.from_station':'BJP',
#     'leftTicketDTO.to_station':'SHH',
#     'purpose_codes':'ADULT'
#     }
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
# data = parse.urlencode(data).encode('utf-8')
# rep = request.Request(url=url,headers=header,data=data)
# html = opener.open(rep).read().decode('utf-8')
print(html)