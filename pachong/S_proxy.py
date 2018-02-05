import  urllib.request
import urllib.error
import random
import requests
from bs4 import BeautifulSoup
import threading
import datetime


def write(path, text):
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
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko"
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {"User-Agent":UserAgent}
    return headers

def  check_ip(targeturl, ip):
    headers =get_UserAgent()
    proxies = {"http": "http://"+ip, "https": "http://"+ip}
    try:
        response=requests.get(url=targeturl,proxies=proxies,headers=headers,timeout=5).status_code
        if response == 200 :
            return True
        else:
            return False
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        return False
    except Exception as e:
        print("Check_ip---Error--->" + str(e))
        return False

def find_ip(type, pagenum, targeturl, path):
    type_list = {
        '1' : 'http://www.xicidaili.com/nt/',
        '2' : 'http://www.xicidaili.com/nn/',
        '3' : 'http://www.xicidaili.com/wn/',
        '4' : 'http://www.xicidaili.com/wt/'
    }
    url =  type_list[str(type)] + str(pagenum)
    print(url)
    headers = get_UserAgent()
    try:
        html =  requests.get(url=url, headers=headers, timeout=5).text
        soup = BeautifulSoup(html, 'lxml')
        all = soup.find_all('tr', class_='odd')
        for i in all:
            t = i.find_all('td')
            ip = t[1].text + ':' + t[2].text
            print("Checking IP :%s now!" % ip)
            is_avail = check_ip(targeturl, ip)
            if is_avail == True:
                write(path=path, text=ip)
                print(ip)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except Exception as e:
        print("find_ip---Error--->"+ str(e))

def  get_ip(targeturl, path):
    threads = []
    for type in range(4):
        for pagenum in range(3):
            t = threading.Thread(target=find_ip, args=(type+1, pagenum+1, targeturl, path))
            threads.append(t)
    print("----------开始爬取代理IP----------")
    for s in threads:
        s.start()
    for e in threads:
        e.join()
    print("-------------爬取完成------------")
if __name__ == '__main__':
    path = "./ip.txt"
    cleanfile(path)
    url = "https://www.baidu.com/"
    start = datetime.datetime.now()
    get_ip(targeturl=url, path=path)
    ips = read(path)
    end = datetime.datetime.now()
    diff = gettimediff(start, end)
    print("一共爬取代理IP：%s个，耗时：%s \n" % (len(ips), diff))