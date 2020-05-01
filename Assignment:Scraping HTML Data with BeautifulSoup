import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')
html = urllib.request.urlopen(link, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
content = []
count = 0
for tag in tags:
    count += 1
    content.append(int(tag.contents[0]))

print('Count {}'.format(count))
print('Sum {}'.format(sum(content)))
