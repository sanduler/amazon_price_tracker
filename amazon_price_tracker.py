# Name: Ruben Sanduleac
# Date: March 3, 2022
# Description: This program uses BeautifulSoup to scrape the price of a specified item from
#              Amazon website. The specifies a target price and the program compares the actual price of
#              to it. Once the price is at or bellow the target price the user is notified with an email.

import requests
from bs4 import BeautifulSoup
import os

# TODO 1: Find an URL to track
URL = "https://www.amazon.com/All-Clad-Nonstick-Anodized-13-Piece-Cookware/dp/B01H93PSKW"
# TODO 2: Use the http://myhttpheader.com/ to find the header needed
headers = {
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8,ms;q=0.6",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4707.0 Safari/537.36"
}
response = requests.get(url=URL, headers=headers)
web = response.text
# print(web)
soup = BeautifulSoup(web, "html.parser")
print(soup)
# TODO 3: Use the requests library to request the HTML page of the Amazon product using the URL
# TODO 4: Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml"
#      parser instead of the "html.parser" for this to work.
# TODO 5: Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
