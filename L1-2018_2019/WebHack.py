# DISCLAIMER : This file was made after a small conference about web security and Python, the web server behind that adress isn't up anymore, so the program will fail. It isn't made to actually hack real, daily websites.

import base64
import requests
from bs4 import BeautifulSoup

url = "http://51.15.129.164"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
secret = soup.find('p', id='secret').text
secret_dec = base64.b64decode(secret).decode()

header = secret_dec.split('"')[3]
html2 = requests.get(url, headers={'Admin': header})
print(html2.content)
