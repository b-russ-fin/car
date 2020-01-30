import requests
from bs4 import BeautifulSoup

URL = "https://www.carspecs.us/cars/2017/acura/mdx/68378"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
