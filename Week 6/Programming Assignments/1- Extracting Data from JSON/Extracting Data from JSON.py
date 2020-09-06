import urllib.request as ur
import json

json_url = input("Enter URL: ")
print("Retrieving ", json_url)

data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')

json_data = json.loads(data)

sum = 0
count_numbers = 0

for comment in json_data['comments']:
    sum += int(comment['count'])
    count_numbers += 1

print('Count:', count_numbers)
print('Sum:', sum)