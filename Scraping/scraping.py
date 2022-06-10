#Beautiful soup - library used in python to scrape websites
#and it allows us to use html and grab different data
#Request modules allows us to download the initial html

import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/news')
#print(res.text)
#html parser converts string html to list that is understood.
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)

#BeautifulSoup Selector allows us to access data using Css
#print(soup.select('.score'))
print(soup.select('.storylink')[0])
links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0])
print(votes.get('score_20154755'))

#Hackers News project
def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        if 
        title = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append({'title': title, 'link':href})
        points = int(votes[idx].getText())
        return hn
print(create_custom_hn(links, votes))
vote = subtext[idx].getText().replace('points')
print(points)
if len(vote):
    points = int(vote[0].getText().replace)(' points', '')
    hn.append({'title': title, 'link': href, 'votes':points})
    return hn
    pprint.pprint(create_custom_hn(links, subtext))
    #pprint- module that prints code in order with spacing

    #Hacker news project 3- SORTS
    def sort_stories_by_votes(hnlist):
    #whenever we sort a list we use key
    return sorted(hnlist,key=lambda k:k['votes'], reverse = True)

#What to do next with scraping
#Scrapy the framework,API.