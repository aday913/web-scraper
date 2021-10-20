from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
URL = 'https://www.amazon.com/House-Suns-Alastair-Reynolds/dp/0316462624/ref=tmm_pap_swatch_0?_encoding=UTF8&coliid=I8NBYXQ5B55M9&colid=1ZGJ9HISC21A9&qid=&sr=&pldnSite=1'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'}

r = s.get(URL, headers=header)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find(id='price')

print(results)