from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://stage.raptorsupplies.com/p/304638"

def get_category_winner(category_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    category = soup.find("img", "fotorama__img")
    winner = soup.find("dd", "sku")
    return {"category": category,
            "category_url": category_url,
            "winner": winner}

