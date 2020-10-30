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


otto = Shop(
    "Otto",
    "https://www.otto.de/p/playstation-5-1154028000/",
    "x",
    "button",
    "p_message__button js_message__close")



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
                        messages=["PS5 Verfügbar bei " + name + " Klick hier: " + url])
        except:
            ava = "Bot detected"
    return ava



print(otto.name + " " + checkShop(otto.name, otto.url, otto.nonavibstr, otto.attrib, otto.classname))

