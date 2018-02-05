import urllib.request
import urllib.parse
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context
cjar = http.cookiejar.CookieJar()
# url= 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LFhBE'
url = 'https://www.m-ebaby.com/index.php?method=customer/login'
header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
opener.addheaders = [header]
urllib.request.install_opener(opener)
# postdata = urllib.parse.urlencode({'username':'81576870',
#              'password':'wjl199122',
#              }).encode("utf-8")

postdata = urllib.parse.urlencode({
    'mobile':'15052610662',
    'loginPW':'019b21595943784bff6834ebb624baa2',
    'channel':'pc'}).encode("utf-8")
req =  urllib.request.Request(url=url,data=postdata)
res = opener.open(req).read()
with open("./home.html","wb") as f:
    f.write(res)
data = urllib.request.urlopen("http://www.xicidaili.com/nt/1").read()
with open("./index2.html","wb") as s:
    s.write(data)

