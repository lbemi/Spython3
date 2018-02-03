from urllib import request,error
from http import cookiejar
import re
x = 1
def get_html(url):
    cjar = cookiejar.CookieJar()
    header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
    opener = request.build_opener(request.HTTPCookieProcessor(cjar))
    opener.addheaders = [header]
    request.install_opener(opener)
    data = request.urlopen(url).read()
    pa = '<div id="plist".+? <div class="page clearfix">'
    p = '<img width="220" height="220" data-img="1" src="//(.+?\.[jpg|png]+)"'
    result = re.compile(pa).findall(str(data))
    r2 = re.compile(p).findall(str(result))
    global x
    for pu in r2:
        try:
            image_dir = "E:\\wechat_jump_game-master\\images\\"+pu.split('/')[-1]
            image_url = "http://"+pu
            request.urlretrieve(image_url, image_dir)
            print("第%s个下载完成！" % str(x))
        except error.URLError as e:
            if hasattr(e,"code"):
                x += 1
                print(e.code)
            if hasattr(e,"reason"):
                x += 1
                print(e.reason)
        x += 1

for i in range(1,100):
    url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
    get_html(url)