import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))


for i in range(0,count):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    print('Retrieving:',tags[position-1].get('href', None))
    link = str(tags[position-1].get('href', None))
