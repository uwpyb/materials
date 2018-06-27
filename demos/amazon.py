# check the price of something on Amazon
import requests
import re
from bs4 import BeautifulSoup

#page = requests.get("https://www.amazon.ca/BOSS-Audio-Distortion-Guitar-Pedal/dp/B0002KYY14/")
page = requests.get("http://a.co/c6kfXSW")
soup = BeautifulSoup(page.content, 'html.parser')
price_text = soup.find_all(id="priceblock_ourprice")[0].text
price_val = float(re.search(r"[0-9]+\.[0-9]+", price_text).group(0))

if price_val < 100.:
    print("TIME TO BUY!")
