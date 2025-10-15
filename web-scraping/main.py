# web load -> parsing -> HTML tree Travsal -> extracting data -> transform of data

import requests
from bs4 import BeautifulSoup

url = "https://www.britannica.com/topic/list-of-countries-1993160"

web = requests.get(url)

# print(web)
# print(web.status_code)
# print(web.content)

soup = BeautifulSoup(web.content, "html.parser")

# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)

# print(soup.p)
# print(soup.h3)
