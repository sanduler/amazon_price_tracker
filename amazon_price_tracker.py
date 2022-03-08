# Name: Ruben Sanduleac
# Date: March 3, 2022
# Description: This program uses BeautifulSoup to scrape the price of a specified item from
#              Amazon website. The specifies a target price and the program compares the actual price of
#              to it. Once the price is at or bellow the target price the user is notified with an email.

import requests
from bs4 import BeautifulSoup
import os

# TODO 1: Find an URL to track
URL = "https://www.amazon.com/All-Clad-Nonstick-Anodized-13-Piece-Cookware/dp/B01H93PSKW/ref=sr_1_9?crid=3PXWMYFCZ7AS9&keywords=all-clad+set&qid=1646698409&sprefix=all-clad+set%2Caps%2C129&sr=8-9"
# TODO 2: Use the http://myhttpheader.com/ to find the header needed
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
accepted_language = "en-US,en;q=0.9,ru;q=0.8"

amazon_header = {
    "Request Line": "GET / HTTP/1.1",
    "User-Agent": user_agent,
    "Accept-Language": accepted_language,
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

}
response = requests.get(url=URL, headers=amazon_header)
print(response.text)
# TODO 3: Use the requests library to request the HTML page of the Amazon product using the URL
# TODO 4: Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml"
#      parser instead of the "html.parser" for this to work.
# TODO 5: Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
