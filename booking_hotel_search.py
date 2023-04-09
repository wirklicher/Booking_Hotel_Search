from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json
import re


class Hotel:
    def __init__(self, name, rating, rating_count, price):
        self.name = name
        self.rating = rating
        self.rating_count = rating_count
        self.price = price
    
    def gimmeInfo(self):
        print(f"Hotel se jmenuje: {self.name}")
        print(f"Jeho hodnocení je {rating} a celkem za dobu své existence obdržel na booking.com {rating_count} recenzí!")
        print(f"Cena za určenou dobu je {price}")



webdriver_service = Service("./chromedriver")
driver = webdriver.Chrome(service=webdriver_service,)
driver.minimize_window()




dest = "Brighton"
checkin = '2023-07-16'
checkout = '2023-07-18'
group_adults = '1'
group_children = '0'
numberRooms = '1'





def geturl():
    '''It tries to build an url based on retrieved parameters from an user'''
    '''dest = input('Zadej destinaci: ')
    checkin = input('Zadej den příjezdu ve tvaru YYYY-MM-DD: ')
    checkout = input('Zadej den odjezdu ve tvaru YYYY-MM-DD: ')'''
    urlbooking = f'https://www.booking.com/searchresults.cs.html?ss={dest}&ssne={dest}&ssne_untouched={dest}&lang=cs&checkin={checkin}&checkout={checkout}&group_adults={group_adults}&no_rooms={numberRooms}&group_children={group_children}'
    return urlbooking

driver.get(geturl())
time.sleep(5)


doc = BeautifulSoup(driver.page_source, "lxml")

for u in doc.select('div[data-testid="property-card"]'):
    title = u.select_one('div[class="fcab3ed991 a23c043802"]').get_text(strip=True)
    rating_count = u.select_one('div[class="d8eab2cf7f c90c0a70d3 db63693c62"]').get_text(strip=True)
    price = u.select_one('span[class="fcab3ed991 fbd1d3018c e729ed5ab6"]').get_text(strip=True)
    for d in doc.select('div[data-testid="review-score"]'):
        rating = u.select_one('div[class="b5cd09854e d10a6220b4"]').get_text(strip=True)
    a = Hotel(title, rating, rating_count, price)
    a.gimmeInfo()

num = doc.select_one('div[class="d8f77e681c"]').getText(strip=True)
a = [int(s) for s in num.split() if s.isdigit()]
a = (a[0] / 25)
print(a)

