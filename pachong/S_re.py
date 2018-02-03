import re
p = "\wp.*?n"
p2 = "\w\dpython[xyz]\w"
p3 = "\w\dpython[^xyz]\w"
p4 = "php|python"
p5 = ".python."
p6 = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = 'aspythondbphp3453pythonaxwyz$%y_py6326'
string2 = "<a herf =http://www.wjlweb.com> TEST</a>"
string3 = 'src = "//img12.360buyimg.com/n7/jfs/t7054/206/2644055615/66333/9e6739b5/598d6ddfN21c4e62c.jpg"'
p8 = "//(.*[.jpg|.png])"
r = re.search(p, string,re.I)
print(r)
print(re.search(p2, string))
print(re.search(p3, string))
print(re.search(p4, string,re.I))
print(re.match(p5, string))
rs = re.compile(p5,re.I).findall(string)
print(rs)
rs2 = re.sub(p5,'***',string,1)
print(rs2)
print(re.sub(p5,'***',string,2))
print(re.compile(p6).findall(string2))
p7 = "[a-zA-Z]+://\S*[.com|.cn]"
print(re.search(p7,string2).span())
print(re.compile(p8).findall(string3))