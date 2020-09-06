import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

count_numbers = 0
sum = 0

print('Retrieving data from: ', url)
xml = ur.urlopen(url).read()
print('Retrieved data: ', len(xml), 'characters')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    count_numbers += 1

print('Count:', count_numbers)
print('Sum:', sum)
