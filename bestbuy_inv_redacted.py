    """
    API authentication token / phone numbers redacted in this file
    """


from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime as dt
import time
import os
from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

links = {
"normalGrey": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-grey-joy-con/13817626",
"normalRB": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625",
"grey": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-lite-grey/13807347",
"turquoise": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-lite-turquoise/13807348",
"yellow": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-lite-yellow/13807346",
"coral": "https://www.bestbuy.ca/en-ca/product/nintendo-switch-lite-coral/14457223"}

times = {c:dt.strptime("200101", "%y%m%d") for c in links}
status = {c:True for c in links}

while True:
    os.system ('cls')
    print (f"<<<  {dt.now()}  >>>")
    for color in links:
        site = urllib.request.urlopen (links [color])
        soup = BeautifulSoup (site.read(), "lxml")
        addToCart = soup.find ("div", {"class": "addToCartContainer_2uzan"})
        if "disabled" in str (addToCart):
            if status[color]:
                status[color] = False

            print (f"{color:<12} OOS since:", times[color].strftime("%b-%d %H:%M"))
        elif "regular" in str (addToCart):
            times [color] = dt.now()
            if not status[color]:
                status[color] = True
                if "normal" in color:
                    message = client.messages \
                                    .create(
                                         body=f"{color} IS INSTOCK AHAHHAHHHHAHHAH",
                                         from_='',
                                         to=''
                                     )
            print (f"{color:<12} IN STOCK")
        else:
            print (color, addToCart)
    time.sleep (10)
