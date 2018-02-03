'''
Tips:
1.多线程
2.代理
3.队列
Create time : 2018-01-30
Author : Cracer
'''
import re
import urllib.request
import time
import urllib.error
import threading,queue

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
opener  = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
listurl =[]
urlqueue = queue.Queue()
def use_proxy(proxy_addr, url):
    try:
        proxy =  urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        with open("./home.html",'wb') as  s:
            s.write(data.encode('utf-8'))
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"reason"):
            print(e.reason)
        if hasattr(e,"code"):
            print(e.code)
        time.sleep(7)
    except Exception as e:
        print("Proxy--Error ----> " + str(e))
        time.sleep(1)


class get_url(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        super().__init__()
        self.key = key
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue =  urlqueue
    def run(self):
        page = self.pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote("&page=")
        for page in range(pagestart, pageend + 1):
            # url = "http://weixin.sogou.com/weixin&type=2?&s_from=input&ie=utf8&_sug_=y&_sug_type_=&w=01019900&query="+keycode+pagecode+str(page)
            url = 'http://weixin.sogou.com/weixin?type=2&query=%E7%89%A9%E8%81%94%E7%BD%91&ie=utf8&_sug_=n&_sug_type_=1&s_from=input&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1517291752074&lkt=0%2C0%2C0&p=40040108'
            data1 = use_proxy(proxy, url)
            # data1 = urllib.request.urlopen(url).read()
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(str(data1)))
        print("total get " + str(len(listurl)) + "pages")
        for i in range(0, len(listurl)):
            time.sleep(5)
            for j in range(0, len(listurl[i])):
                try:
                    url = listurl[i][j]
                    url = url.replace('amp;', '')
                    print("第 "+ str(i) + 'i' +str(j) + 'j次入队 ')
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except urllib.error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                except Exception as e:
                    print("Get_url--Error ----> " + str(e))

class get_content(threading.Thread):
    def __init__(self, urlqueue, proxy):
        super().__init__()
        self.urlqueue = urlqueue
        self.proxy =  proxy

    def run(self):
        i = 1
        html1 = '''     <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>微信文章页面</title>
        </head>
        <body>
        '''
        with open('./wx.html', 'wb') as  f:
            f.write(html1.encode('utf-8'))
        f = open('./wx.html', 'ab')
        while True:
            try:
                url = urlqueue.get()
                data = use_proxy(proxy, url)
                # data = urllib.request.urlopen(url).read().decode('utf-8')
                titlepat = "<title>(.*?)</title>"
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(titlepat, re.S).findall(data)
                print(title)
                content = re.compile(contentpat, re.S).findall(data)
                thistitle = "Can't get title!!"
                thicontent = "Cant't get content!"
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thicontent = content[0]
                dataall = "<p> title is :" + thistitle + "</p><p> Content is :" + thicontent + "</p><br>"
                f.write(dataall.encode('utf-8'))
                print("第"+str(i)+"个网页处理")
                i += 1
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
                time.sleep(7)
            except Exception as e:
                print("Get_conten--Error ---> " + str(e))
                time.sleep(1)
        f.close()
        html2 = '''   
        </body>
        </html>
            '''
        with open('./wx.html', 'ab') as  f:
            f.write(html2.encode('utf-8'))

class control(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
    def run(self):
        while(True):
            print("程序执行中...")
            time.sleep(30)
            if (self.urlqueue.empty()):
                print("程序执行完毕！！")
                exit()

key = "物联网"

proxy = '61.144.105.117:9797'
proxy2 = ""
pagestart = 1
pageend = 2
t1 = get_url(key, pagestart, pageend, proxy, urlqueue)
t1.start()

t2 = get_content(urlqueue, proxy)
t2.start()

t3 = control(urlqueue)
t3.start()

# def get_url(key, pagestart, pageend, proxy):
#     try:
#         page =  pagestart
#         keycode = urllib.request.quote(key)
#         pagecode = urllib.request.quote("&page=")
#         for page in range(pagestart, pageend+1):
#             # url = "http://weixin.sogou.com/weixin&type=2?&s_from=input&ie=utf8&_sug_=y&_sug_type_=&w=01019900&query="+keycode+pagecode+str(page)
#             url = 'http://weixin.sogou.com/weixin?type=2&query=%E7%89%A9%E8%81%94%E7%BD%91&ie=utf8&_sug_=n&_sug_type_=1&s_from=input&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1517291752074&lkt=0%2C0%2C0&p=40040108'
#             data1 = use_proxy(proxy, url)
#             # data1 = urllib.request.urlopen(url).read()
#             listurlpat = '<div class="txt-box">.*?(http://.*?)"'
#             listurl.append(re.compile(listurlpat, re.S).findall(str(data1)))
#         print("total get "+ str(len(listurl)) + "pages")
#         print(listurl[0])
#         return listurl
#     except urllib.error.URLError as e:
#         if hasattr(e,"code"):
#             print(e.code)
#         if hasattr(e,"reason"):
#             print(e.reason)
#     except Exception as e:
#         print("Get_url--Error ----> "+ str(e))

# def get_content(listurl,proxy):
#     i = 1
#     html1 = '''     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>微信文章页面</title>
# </head>
# <body>
# '''
#     with open('./wx.html','wb') as  f:
#         f.write(html1.encode('utf-8'))
#     f = open('./wx.html','ab')
#     for i in range(0, len(listurl)):
#         for j in range(0, len(listurl[i])):
#             try:
#                 url = listurl[i][j]
#                 url = url.replace('amp;','')
#                 data = use_proxy(proxy, url)
#                 # data = urllib.request.urlopen(url).read().decode('utf-8')
#                 titlepat = "<title>(.*?)</title>"
#                 contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
#                 title = re.compile(titlepat,re.S).findall(data)
#                 print(title)
#                 content = re.compile(contentpat,re.S).findall(data)
#                 thistitle = "Can't get title!!"
#                 thicontent = "Cant't get content!"
#                 if (title != []):
#                     thistitle = title[0]
#                 if (content != []):
#                     thicontent = content[0]
#                 dataall = "<p> title is :"+ thistitle+"</p><p> Content is :"+thicontent+"</p><br>"
#                 f.write(dataall.encode('utf-8'))
#                 print("The " + str(i) +" page " + str(j) +"handle!")
#             except urllib.error.URLError as e:
#                 if hasattr(e,'code'):
#                     print(e.code)
#                 if hasattr(e,'reason'):
#                     print(e.reason)
#                 time.sleep(7)
#             except Exception as e:
#                 print("Get_conten--Error ---> "+ str(e))
#                 time.sleep(1)
#     f.close()
#     html2 = '''
# </body>
# </html>
#     '''
#     with open('./wx.html','ab') as  f:
#         f.write(html2.encode('utf-8'))



