from bs4 import BeautifulSoup
import lxml.html
from lxml import etree

import requests
print("starting:")
product=input("get some: ")

bot = requests.get(f"https://bikroy.com/en/ads/dhaka?sort=relevance&buy_now=0&urgent=0&query={product}&page=1").text
soup = BeautifulSoup(bot,"lxml")
phones = soup.find_all("li",class_="normal--2QYVk gtm-normal-ad")

for phone in phones:
    phone_model = phone.find("h2",class_="heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow").text.replace(" ","")
    adress = phone.find("div",class_="description--2-ez3").text.replace(" ","")
    price = phone.find("div",class_="price--3SnqI color--t0tGX").text.replace(" ","")
    time = phone.find("div",class_ = "updated-time--1DbCk").text.replace(" ","")
    link = phones.x



    print(link)
    print(f" Phone Name:{phone_model.strip()}")
    print(f" Address: {adress.strip()}")
    print(f" Price: {price.strip()}")
    print(f"Upload time: {time}")


    print("")
