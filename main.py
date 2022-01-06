import telegram_send
from bs4 import BeautifulSoup
import time
import datetime
import os.path as path
import requests
import logging as log
requests.packages.urllib3.disable_warnings()
import random

randomint = random.randrange(0,55)
randomwait = random.randrange(1,10)
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/517.{} (KHTML, like Gecko) Chrome/79.0.3945.88".format(randomint)

headers = {'User-Agent': agent}


class Shop:
    def __init__(self, name, url, nonavibstr, attrib, classname):
        self.name = name
        self.url = url
        self.nonavibstr = nonavibstr
        self.attrib = attrib
        self.classname = classname


# amazon = Shop(
#     "Amazon",
#     "https://www.amazon.de/dp/B08H93ZRK9/ref=twister_B08JVHJNHG?_encoding=UTF8&th=1",
#     "Derzeit nicht verfügbar.",
#     "span",
#     "a-size-medium a-color-price")

denon = Shop(
    "Denon",
    "https://www.denon.com/de-de/product/special/avc-x3700h-r/",
    "Momentan nicht verfügbar",
    "button",
    "btn")


Shops = [denon]


def checkShop(name, url, nonavibstr, attrib, classname):
    response = requests.get(url, headers=headers, verify=False)
    if response.history:
        ava = "NO"
    else:
        soup = BeautifulSoup(response.content, "html.parser")
        avail = soup.find(attrib, class_= classname)
        ava = "NO"
        try:
            if avail is not None:
                value = avail.string
                if (value.strip()) != nonavibstr:
                    ava = "YES"
                    telegram_send.send(
                        messages=["Artikel Verfügbar bei " + name + " Klick hier: " + url])
        except:
            ava = "Bot detected"
    return ava

print("Lurking for Article availibility...")
print([i.name for i in Shops])
while True:

    for i in Shops:
        if [checkShop(i.name, i.url, i.nonavibstr, i.attrib, i.classname)] == "YES":
            print(i.name )

    time.sleep(30)
    pass
