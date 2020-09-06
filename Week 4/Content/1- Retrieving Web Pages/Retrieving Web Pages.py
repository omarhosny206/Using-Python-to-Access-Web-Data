# this library does all the socket work and make web pages look like a file
import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in file_handle:
    print(line.decode().strip())

print('.' * 100)

file_handle_ = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line_ in file_handle_:
    print(line_.decode().strip())

# this program is the improvement of week 3.
