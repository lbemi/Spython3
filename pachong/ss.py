'''
1、显示下载进度条
2、
'''
import os
import urllib.request
import requests, re, time
from tqdm import tqdm
urls = "http://download.adobe.com/pub/adobe/magic/photoshop/win/8.x/AdobePhotoshopCS.zip"
targetPath = "e:\\wechat_jump_game-master\\download"

url = "https://www.douban.com/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
req = urllib.request.Request(url=url,headers=header)
res = urllib.request.urlopen(req)
data = res.read()


# for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
#     print(link)
#     try:
#         urllib.request.urlretrieve(link,saveFile(link))
#     except Exception as e:
#         print("Error-->" + str(e))

def savePath(path):  #存储路径
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t

def download_from_url(url):
    try:
        dst = savePath(url)
        file_size = int(urllib.request.urlopen(url).info().get('Content-Length', -1))
        # if os.path.exists(dst):
        #     first_byte = os.path.getsize(dst)
        #     first_byte = 0
        #     print("File have existed!! \nContinue recover please input 'Y'!")
        #     i = input()
        #     if i == 'y':
        #         os.remove(dst)
        #         first_byte = 0
        #     else:
        #         quit()
        # else:
        first_byte = 0
        if first_byte >= file_size:
            return file_size
        header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
        pbar = tqdm(
            total=file_size, initial=first_byte,
            unit='B', unit_scale=True, desc=url.split('/')[-1])
        req = requests.get(url, headers=header, stream=True)
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
        return file_size
    except Exception as e:
        print("Error ---> " + str(e))


for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    # print(link+'\n')
    download_from_url(link)
    time.sleep(0.2)
