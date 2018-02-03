import requests
import urllib.request
type_list = {
    "1": 'http://www.xicidaili.com/nt/',
    '2': 'http://www.xicidaili.com/nn/',
    '3': 'http://www.xicidaili.com/wn/',
    '4': 'http://www.xicidaili.com/wt/'
}
type = 1
pagenum =1
url = type_list[str(type)] + str(pagenum)
headers= ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko")
targeturl = "https://movie.douban.com/"
proxy = ""
ip = '117.117.196.9:80'
def check_IP(targeturl, ip):
    print(">>>Check_Ip<<<<")
    proxy = urllib.request.ProxyHandler({"http":ip,"https":ip})
    # try:
    opener = urllib.request.build_opener(urllib.request.HTTPHandler,proxy)
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    print("aaaaaaaaaaaaaaaaaaaa")
    result = urllib.request.urlopen(targeturl, timeout=5)
    print(result.getcode())
    # res_code = requests.get(url=targeturl, headers=headers, proxies=proxy, timeout=5).status_code
    # print(res_code)
    # if res_code == 200:
    #     return True
    # else:
    #     return False

a = check_IP(targeturl, ip)
# res_code = requests.get(targeturl, headers, timeout=5).status_code
# print(res_code)
print(a)