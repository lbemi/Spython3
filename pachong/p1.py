import urllib.parse
import urllib.request
import urllib.error

# header =  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
# # rep = urllib.request.Request(url=url,headers=header)
# # res = urllib.request.urlopen(rep)
# # data = res.read()
# opener = urllib.request.build_opener()
# opener.addheaders =  [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")]
# # data = opener.open(url).read()
# postdata = urllib.parse.urlencode({"name":"admin",
#             "pass":"test"
#             }).encode("utf-8")
# data = opener.open(url, postdata).read()
#
# with open("./p1.html","wb") as file:
#     file.write(data)



def  use_proxy(url):
    try:
        # proxy =  urllib.request.ProxyHandler({"http":proxy_addr})
        # opener =  urllib.request.build_opener(proxy,  urllib.request.HTTPHandler(debuglevel=1))
        # urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except urllib.error.URLError as e:
        print(str(e))
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    #     print(e.code)
    #     print(e.reason)
    # except urllib.error.HTTPError as e:
    #     print(e.reason)


proxy_addr = "122.225.17.123:8080"
url = "https://www.sssm-ebaby.com/frontssss/"
data = use_proxy(url)




