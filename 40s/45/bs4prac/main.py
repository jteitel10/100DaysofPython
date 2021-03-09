from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
ycombo_response = requests.get(url=url)
ycombo_response.raise_for_status()
data = ycombo_response.text

soup = BeautifulSoup(data, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))
article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]
# print(article_upvote)
# print(article_texts)
# upvote_num = int(article_upvotes[0].split()[0])
max_num = max(article_upvotes)
max_index = article_upvotes.index(max_num)
print(article_texts[max_index] + " : " + article_links[max_index])
