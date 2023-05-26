from bs4 import BeautifulSoup
import requests

################################################
#                                              #
#  Make sure to check /robots.txt              #
#  Before Scraping                             #
#                                              #
################################################



response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_tag = soup.find_all("span","titleline")
article_texts=[]
article_links=[]
for article in article_tag:
    article_text = article.get_text()
    article_texts.append(article.text)
    article_link = article.find("a")["href"]
    article_links.append(article_link)
# article_text = article_tag.get_text()
# article_link = article_tag.find("a")["href"]
# article_upvote=soup.find("span","score").get_text()
#article_upvote = [score.get_text() for score in soup.find_all("span","score")]
article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all("span","score")]
largest_number = max(article_upvote)
larget_index = article_upvote.index(largest_number)
print(article_texts[larget_index])
print(article_links[larget_index])
# print(article_texts)
# print(article_links)
# print(article_upvote)























# with open("website.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title.string)
# # print(soup.findAll("p"))
#
# for tag in soup.find_all("a"):
#     print(tag.get("href"))