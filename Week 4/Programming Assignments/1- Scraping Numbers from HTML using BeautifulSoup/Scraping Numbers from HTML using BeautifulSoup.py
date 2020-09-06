import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# SSL --> stands for Secure Sockets Layer and is designed to create secure connection between client and server. It also allows to validate server identity.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
spans = soup('span')
count = 0
sum = 0
for span in spans:
    count += 1
    sum += int(span.contents[0])

print('Count ', count)
print('Sum ', sum)

# this program is the improvement of week 3.
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_913790.html