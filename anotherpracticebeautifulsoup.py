from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"

response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

title_list = []
link_list = []
votes_list = []

articles = soup.select(selector=".titleline")
for art in articles:
    articles_title = art.get_text()
    title_list.append(articles_title)
    articles_link =art.select_one(selector="a")
    articles_link = articles_link.get("href")
    link_list.append(articles_link)

articlesvote = soup.select(selector=".score")
for votes in articlesvote:
    articles_vote = votes.get_text()
    number = articles_vote.split()[0]
    votes_list.append(int(number))

print(title_list)
print(link_list)
print(votes_list)    

max_votes = max(votes_list)
max_indices = votes_list.index(max_votes)

print(title_list[max_indices])
print(link_list[max_indices])
print(max_votes)


