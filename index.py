from flask import Flask
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime as dt
import time
import os
from twilio.rest import Client
account_sid = 'ACb85326194b6825e88c98ec05a59107d2'
auth_token = 'bedbc8baa1fedb4c3b799b5fc394c37f'
client = Client(account_sid, auth_token)

links = {
"grey": "https://www.bestbuy.ca/en-ca/product/13807347",
"turquoise": "https://www.bestbuy.ca/en-ca/product/13807348",
"yellow": "https://www.bestbuy.ca/en-ca/product/13807346",
"coral": "https://www.bestbuy.ca/en-ca/product/14457223"}

def munny ():
    response = f"///  {dt.now()}  /// <br>"
    for color in links:
        site = urllib.request.urlopen (links [color])
        soup = BeautifulSoup (site.read(), "lxml")
        addToCart = soup.find ("div", {"class": "addToCartContainer_2uzan"})
        if "disabled" in str (addToCart):
            response += f"{color:<12} &nbsp out of stock <br>"
        elif "regular" in str (addToCart):
            if color == "coral":
                message = client.messages \
                                .create(
                                     body="CORAL IS INSTOCK AHAHHAHHHHAHHAH",
                                     from_='+18636243631',
                                     to='+16479968291'
                                 )
                break
            response += f"{color:<12} &nbsp IN STOCK <br>"
        else:
            print (color, addToCart)
    return response

app = Flask(__name__)

@app.route("/")
def hello():
    response = f"///  {dt.now()}  /// <br>"
    for color in links:
        site = urllib.request.urlopen (links [color])
        soup = BeautifulSoup (site.read(), "lxml")
        addToCart = soup.find ("div", {"class": "addToCartContainer_2uzan"})
        if "disabled" in str (addToCart):
            response += f"{color:<12} out of stock <br>"
        elif "regular" in str (addToCart):
            if color == "coral":
                message = client.messages \
                                .create(
                                     body="CORAL IS INSTOCK AHAHHAHHHHAHHAH",
                                     from_='+18636243631',
                                     to='+16479968291'
                                 )
                break
            response += f"{color:<12} IN STOCK <br>"
        else:
            print (color, addToCart)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)