
import urllib.request

url = 'https://raw.githubusercontent.com/bol-van/rulist/main/reestr_hostname.txt'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

hostnames = text.split('\n')

f = open("proxy_list.txt", "a")

for hostname in hostnames:
    if len(hostname) > 0:
        modified = '(?:^|\.)' + hostname.replace('.', '\.') + '$'
        f.write(modified + '\n')

f.close()
