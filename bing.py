import requests
from bs4 import BeautifulSoup
import re
import shutil

url = 'https://cn.bing.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'lxml')
pret = soup.prettify()
img = soup.find(attrs={'id': 'bgLink'})
fhref = img['href']
pattern = re.compile('=OHR\.(.*?)&')
filename = re.findall(pattern, fhref)
r = requests.get(url + fhref, stream=True, headers=headers)
with open(filename[0], 'wb') as f:
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, f)
print(url + fhref)
print(filename[0])
