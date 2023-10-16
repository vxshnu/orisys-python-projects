#Extract heading scores and links of ycombinator site 
import re
from bs4 import BeautifulSoup
import requests
response=requests.get("https://news.ycombinator.com/")
soup=BeautifulSoup(response.text,"html.parser")
all_code=soup.find_all(name='span',attrs={"class":"titleline"})
all_score=soup.find_all(name='span',attrs={"class":"score"})

all_headings=[]
all_links=[]
all_scores=[]
for span in all_code:
    link = span.find("a")
    all_headings.append(link.get_text())
    all_links.append(link.get("href"))

for i in all_score:
    all_scores.append(i.get_text())
for i in all_headings:
    print(i)
for i in all_links:
    print(i)
for i in all_scores:
    print(i)
