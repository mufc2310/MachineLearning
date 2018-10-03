import requests
from bs4 import BeautifulSoup

html_page = requests.get("https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv")

# print(html_page.text)

soup = BeautifulSoup(html_page.text,"lxml")
for l in soup.find_all('h1'):    #find_all/find
    print(l.text)
# print(soup)

a=soup.find("td",{'class':'titleColumn'})          #classname: tag
a_tag=a.find('a')
print(a_tag.text)

b=soup.find("td",{'class':'lister-list'})
b_tag=a.find('a')
print(b_tag.text)