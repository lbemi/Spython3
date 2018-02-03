import urllib.request ,os , re
targetPath = "e:\\wechat_jump_game-master\\images"
# def saveFile(path):
#     if not os.path.isdir(targetPath):
#         os.mkdir(targetPath)
#     pos = path.rindex('/')
#     t = os.path.join(targetPath,path[pos+1:])
#     return t
#
# url = "https://www.douban.com/"
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
# req = urllib.request.Request(url=url,headers=header)
# res = urllib.request.urlopen(req)
# data = res.read()
#
# for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
#     print(link)
#     try:
#         urllib.request.urlretrieve(link,saveFile(link))
#     except Exception as e:
#         print("Error-->" + str(e))
link = "https://img3.doubanio.com/view/photo/albumcover/public/p2427474252.jpg"
def save(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    print(t)
    return t
def openurl(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
    req = urllib.request.Request(url=url,headers=header)
    res = urllib.request.urlopen(req)
    data = res.read()
    try:
        urllib.request.urlretrieve(url, save(url))
    except Exception as e:
        print("Error-->" + str(e))


if __name__ == '__main__':
    openurl(link)