# # web load -> parsing -> HTML tree Travsal -> extracting data -> transform of data

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# url = "https://www.britannica.com/topic/list-of-countries-1993160"

# web = requests.get(url)

# # print(web)
# # print(web.status_code)
# # print(web.content)

# soup = BeautifulSoup(web.content, "html.parser")

# # print(soup)
# # print(soup.prettify())

# # print(soup.title)
# # print(soup.title.name)

# # print(soup.p)
# # print(soup.h3)


# # print(soup.table)

# # print(len(soup.find_all("table")))

# countries = []
# for table in soup.find_all("table"):
#     caption = table.find("caption").text

#     tbody = table.find("tbody")
#     for tr in tbody.find_all("tr"):
#         country = {}
#         country["name"] = tr.find_all("td")[0].text
#         # country["Letter"] = tr.find_all("td")[0].text[0]
#         country["Letter"] = caption
#         country["geographical region"] = tr.find_all("td")[1].text
#         countries.append(country)
# print(countries)

# df = pd.DataFrame(countries)

# # Save to Excel file
# df.to_excel('countries1.xlsx', index=False)

# print("✅ Excel file 'countries.xlsx' created successfully!")

# letters = "D, E, F".split(",")
# print(letters)

# name = "Jenmark"

# print(name[0] in letters)