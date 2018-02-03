import re
import urllib.request
import urllib.error
import  ssl
import http.cookiejar
def get_content(url,page):
    try:
        c =  http.cookiejar.CookieJar()
        ssl._create_default_https_context = ssl._create_stdlib_context
        header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
        opener =  urllib.request.build_opener(urllib.request.HTTPCookieProcessor(c))
        opener.addheaders = [header]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        user_pat = '<h2>(.*?)</h2>'
        content_pat = '<div class="content">(.*?)</div>'
        user_List = re.compile(user_pat,re.S).findall(data)
        content_list = re.compile(content_pat,re.S).findall(data)
        x = 1
        for content in content_list:
            content =  content.replace("\n","")
            name = "content"+str(x)
            exec(name + '=content')
            x += 1
        y = 1
        for user  in user_List:
            name = "content"+ str(y)
            print("用户"+ str(page) + str(y) + "是："+ user)
            print("内容是：")
            exec ("print ("+name+")")
            print("\n")
            y += 1
    except urllib.error.URLError as e:
        print(e.code)
        print(e.reason)
    return content_list
# for i in range(1,10):
#     url = "https://www.qiushibaike.com/8hr/page/"+ str(i)+"/"
#     get_content(url, i)

url = "https://www.qiushibaike.com/8hr/page/2/"
get_content(url, 2)
with open('./joke.html','wb') as f:
    for i in str(get_content(url, 2)):
        f.write(i)