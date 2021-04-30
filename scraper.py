import requests
from bs4 import BeautifulSoup
import json
import cssutils
import re


page = requests.get('https://www.forbes.com/innovation/#58019b0c6834')

soup = BeautifulSoup(page.text, 'html.parser')
title_classes=["headlink","stream-item__title"]
image_classes=["enhanced style","style"]

extracted_titles = []
extracted_authors=[]
extracted_imgSrc=[]


for each in title_classes:
    obj1=soup.find_all("a",attrs={'class':each})
    for link in obj1: 
        title = link.text
    
        extracted_titles.append(title)



obj2=soup.find_all("a",attrs={'class':'byline__author-name'})
for links in obj2:  
    author = links.text
    
    extracted_authors.append(author)  

# for each1 in image_classes:
# obj4=soup.find_all("div",attrs={'class':'preview__overflow-wrapper'})
images = soup.find_all('.jpg')
for each in images:
    src=each['style']
    sources={
            'imageSrc':src
        }
  
    extracted_imgSrc.append(sources)
print(extracted_imgSrc)



jsonFinal=[]
i=0
for (item1, item2) in zip(extracted_titles, extracted_authors):
    title=extracted_titles[i]
    author=extracted_authors[i]
    i=i+1
    final = {

         'author':author,
         'title':title
        
            }
            
    jsonFinal.append(final)
print(jsonFinal)
with open("/Users/prachisethi/Downloads/google-maps-challenge/js/sample.js", "w") as outfile: 
    json.dump(jsonFinal, outfile) 
