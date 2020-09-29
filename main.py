import telegram_send
from bs4 import BeautifulSoup
import time
import requests
requests.packages.urllib3.disable_warnings()


headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 '
            'Safari/537.36',
            'Accept-Language': 'de-DE, de;q=0.5'})


class Shop:
    def __init__(self, name, url, nonavibstr, attrib, classname):
        self.name = name
        self.url = url
        self.nonavibstr = nonavibstr
        self.attrib = attrib
        self.classname = classname


amazon = Shop(
    "Amazon",
    "https://www.amazon.de/dp/B08H93ZRK9/ref=twister_B08JVHJNHG?_encoding=UTF8&psc=1",
    "Derzeit nicht verfügbar.",
    "span",
    "a-size-medium a-color-price")

otto = Shop(
    "Otto",
    "https://www.otto.de/p/playstation-5-1154028000/",
    "PlayStation 5 Medienfernbedienung",
    "h1",
    "js_shortInfo__variationName prd_shortInfo__variationName")

mm = Shop(
    "MediaMarkt",
    "https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-2661938.html",
    "Dieser Artikel ist aktuell nicht verfügbar.",
    "h4",
    "Typostyled__StyledInfoTypo-sc-1jga2g7-0 dXEylL")

expert = Shop(
    "Expert",
    "https://www.expert.de/shop/unsere-produkte/gaming-freizeit/sony-playstation/playstation-konsolen/11364129744-playstation-r-5.html",
    "Das von Ihnen ausgewählte Produkt ist ausverkauft.",
    "div",
    "widget widget-Text widget-Text---c643eae2-bf63-4f6b-8975-4c2342b06cf3 widget-Text---view-text widget-Text---preset-default margin-xs-top-70 margin-lg-top-0")

gamestop = Shop(
    "GameStop",
    "https://www.gamestop.de/PS5/Games/58665#",
    "Derzeit nicht Verfügbar",
    "a",
    "megaButton buyDisabled")


Shops = [amazon, otto, expert, gamestop]


def checkShop(name, url, nonavibstr, attrib, classname):
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, "lxml")
    avail = soup.find(attrib, class_= classname)
    try:
        value = avail.string
        ava = "NO"
        if (value.strip()) != nonavibstr:
            ava = "YES"
            telegram_send.send(
                messages=["PS5 Verfügbar bei " + name + " Klick hier: " + url])
    except:
        ava = "Bot detected"
    return ava


while True:

    for i in Shops:
        print(i.name + " " + checkShop(i.name, i.url,
                                       i.nonavibstr, i.attrib, i.classname))

    time.sleep(60)
    pass
