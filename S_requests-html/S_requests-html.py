'''
Github:https://github.com/kennethreitz/requests-html
'''
from html2text import HTML2Text
from requests_html import HTML
import requests_html
session = requests_html.Session()
r = session.get('https://python.org/')
res =  r.html.links
res2 = r.html.absolute_links
print(res)
print(res2)

about = r.html.find('#about', first = True)
print(about.text, about.attrs)
# print(str(about.html))

doc = """<a href='https://httpbin.org'>"""
html1 = HTML(html=doc, url='fakeurl', default_encoding='utf-8')
print(html1.links)


h = HTML2Text()
print(h.handle(about.html))