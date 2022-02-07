"""webscrapping"""
import pprint
import requests
from bs4 import BeautifulSoup
from performance_decorator import performance


res = requests.get("https://news.ycombinator.com/news")
docs = BeautifulSoup(res.text, "html.parser")
links = docs.select(".titlelink")
subtext = docs.select(".subtext")


def sorting_feeds(hnlist):
    """sorting function"""
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


@performance
def create_custom_hm(link, subtexts):
    """custom feeds"""
    hacker_news = []
    for idx, item in enumerate(link):
        title = item.get_text()
        href = item.get("href", None)
        vote = subtexts[idx].select(".score")
        if len(vote):
            points = int(vote[0].get_text().replace(" points", ""))
            if points >= 100:
                hacker_news.append(
                    {"title": title, "link": href, "votes": points})
    return sorting_feeds(hacker_news)


pprint.pprint(create_custom_hm(links, subtext))
