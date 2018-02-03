'''
Tips:
1.Get the available agent address
2.Check the agent IP available
3.Url:http://www.xicidaili.com
Create time : 2018-01-30
Author : Cracer

70 Completed!

'''
import urllib.request
from bs4 import BeautifulSoup
import urllib.error
import threading
import requests
import random,datetime

# url = 'http://www.xicidaili.com/nn/'
# header = ("User-Agent",
#           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
# opener =  urllib.request.build_opener()
# opener.addheaders= [header]
# urllib.request.install_opener(opener)
#
# def getProxyIP(url):
#     proxy=[]
#     try:
#         data = urllib.request.urlopen(url).read()
#         with open("./home.html",'wb') as s:
#             s.write(data)
#         soup = BeautifulSoup(data)
#         ips =  soup.find_all('tr')
#         for x in range(1,len(ips)):
#             ip =  ips[x]
#             tds =  ip.findAll('td')
#             ip_temp = tds[1].contents[0]+'\t'+tds[2].contents[0]
#             print(ip_temp)
#             proxy.append(ip_temp)
#     except urllib.error.URLError as e:
#         if hasattr(e,'code'):
#             print(e.code)
#         if hasattr(e,'reason'):
#             print(e.reason)
#     except Exception as e:
#         print("Error ---> "+ str(e))
#     return proxy
# def validateIP(proxy):
#     url = 'http://ip.chinaz.com/getip.aspx'
#     f = open('./proxy.txt','w')
#     socket.setdefaulttimeout(3)
#     for i in range(0,len(proxy)):
#         try:
#             ip = proxy[i].strip().split('\t')
#             proxy_host = "http://" + ip[0]+ ":" + ip[1]
#             proxy_tmp = {"http":proxy_host}
#             res = requests.
#
# if __name__ == '__main__':
#     proxy = getProxyIP(url)
#     with open('./proxy.txt','w') as f:
#         for x in proxy:
#             f.write(x+'\n')

def  write(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text+'\n')

def cleanfile(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write("")

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = []
        for s in f.readline():
            txt.append(s.strip())
    return txt


def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff =  ("%02d:%02d:%02d"%(h, m, s))
    return diff


def get_UserAgent():
    user_agent_list = [
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        # "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        # "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        # "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        # "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        # "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko"
    ]
    UserAgent = random.choice(user_agent_list)
    headers = ("User-Agent",UserAgent)
    return headers

def check_IP(targeturl, ip):
    print(">>>Check_Ip<<<<")
    headers = get_UserAgent()
    proxy =urllib.request.ProxyHandler({"http":ip,"https":ip})
    # try:
    opener.addheaders = [headers]
    opener = urllib.request.build_opener(urllib.request.HTTPHandler,proxy)

    urllib.request.install_opener(opener)
    print("aaaaaaaaaaaaaaaaaaaa")
    res_code = urllib.request.urlopen(targeturl, timeout=5)
    print(res_code.getcode())
    # res_code = requests.get(url=targeturl, headers=headers, proxies=proxy, timeout=5).status_code
    print(res_code)
    if res_code == 200:
        return True
    else:
        return False
    # except urllib.error.URLError as e:
    #     if hasattr(e,"code"):
    #         print(e.code)
    #     if hasattr(e,"reason"):
    #         print(e.reason)
    #     return False
    # except Exception as e:
    #     print("Check_ip---Error--->" + str(e))
    #     return False
    print("<<<<Check_Ip>>>>")
def find_ip(type, pagenum,  targeturl, path):
    print(">>>find_ip<<<")
    type_list = {
        "1" : 'http://www.xicidaili.com/nt/',
        '2' : 'http://www.xicidaili.com/nn/',
        '3' : 'http://www.xicidaili.com/wn/',
        '4' : 'http://www.xicidaili.com/wt/'
    }
    url = type_list[str(type)] + str(pagenum)
    print(url)
    headers = get_UserAgent()
    # print(headers)
    # html = requests.get(url=url, headers=headers, timeout=5).text
    html = urllib.request.urlopen(url, headers, timeout=5).read()
    # print(html.decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    all = soup.find_all('tr', class_='odd')
    # print(all)
    for i in all:
        t = i.find_all('td')
        ip = t[1].text + ':' + t[2].text
        print(ip)
        is_avail =  check_IP(targeturl, ip)
        if is_avail == True:
            write(path, ip)
            print(ip)
    print("<<<<find_ip>>>>")
def get_ip(targeturl, path):
    threads = []
    for type in range(4):
        for pagenum in range(3):
            t = threading.Thread(target=find_ip(type+1, pagenum+1, targeturl, path))
            threads.append(t)
    print("---------------开始爬取代理IP---------------")
    for s in threads:
        s.start()
    for e in threads:
        e.join()

    print("------------------爬取完成------------------")



if __name__ == '__main__':
    # try:
    path = "./ip.txt"
    cleanfile(path)
    url = "https://movie.douban.com/"
    start = datetime.datetime.now()
    get_ip(targeturl=url, path=path)
    ips = read(path)
    end =  datetime.datetime.now()
    diff = gettimediff(start, end)
    print("一共爬取代理IP：%s个，耗时：%s \n"%(len(ips), diff))
    # except urllib.error.URLError as e:
    #     if hasattr(e, "code"):
    #         print(e.code)
    #     if hasattr(e, "reason"):
    #         print(e.reason)
    # except Exception as e:
    #     print("Main--Error--->" + str(e))
