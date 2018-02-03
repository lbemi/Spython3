import re
import urllib.request

def get_all_url(url):
    header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
    opener =  urllib.request.build_opener()
    opener.addheaders = [header]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url).read()
    with open('./home.html','wb') as f:
        f.write(file)
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(str(file))
    link = list(set(link))
    return link

url = "http://blog.csdn.net/"

linklist = get_all_url(url)

for link in linklist:
    print(link[0])