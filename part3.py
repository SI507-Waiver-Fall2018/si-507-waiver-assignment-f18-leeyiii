# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

path = "https://www.michigandaily.com/"

response = requests.get(path)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

mostread = soup.find("aside", {"class": "asidebar"}).find("div", {"class": "panel-pane pane-mostread"}).find("div", {"class": "pane-content"})
mostread_list = mostread.findAll("li")

author_list = []
title_list = []
for node in mostread_list:
    link = node.a["href"]
    title = node.a.get_text()
    title_list.append(title)

    sub_response = requests.get(path + link)
    sub_soup = BeautifulSoup(sub_response.text, "html.parser")
    author_view = sub_soup.find("div", {"class": "view-content"})
    authors = []
    if author_view:
        author_nodes = author_view.findAll("div", {"class": "link"})
        for author_node in author_nodes:
            if author_node != " ":
                authors.append(author_node.get_text())
    else:
        author_view = sub_soup.find("p", {"class": "info"})
        authors.append(author_view.get_text())

    author_list.append(authors)


# output layer
print("Michigan Daily -- MOST READ  ")
for i in range(len(author_list)):
    print(title_list[i])
    if len(author_list[i]):
        print("  " + ", ".join(author_list[i]))

