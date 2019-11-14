# This is Amazon automatic pricing
# When using Email and password please use your own
# Also when using email enable less secure app access from your google account
import requests
import bs4
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/CYBERPOWERPC-Xtreme-i5-9400F-GeForce-GXiVR8060A8/dp/B07VGJDKZ4/ref=lp_8588813011_1_1?' \
     's=electronics&ie=UTF8&qid=1573003904&sr=1-1' \

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'} \

def check_price():
   page = requests.get(URL, headers= headers)
   soup1 = BeautifulSoup(page.content, 'html.parser')
   soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

   # Getting the title and price of the items
   title =  soup2.find(id="productTitle").get_text()
   price = soup2.find(id= "priceblock_ourprice").get_text()

   #converted_price = str(price)
   print(str(price))
   print(title.strip())

   if (price > str(760)):
       send_email(subject, msg)

   elif (price < str(780)):
        print ("It look like this pc is little over price")


def send_email(subject, msg):
    try:
        EMAIL_ADDRESS = ("alexnt2357@gmail.com")
        EMAIL_PASSWORD = ("wgbynrdlrcpbmkbk")
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject,msg)
        server.sendmail( EMAIL_ADDRESS,  EMAIL_ADDRESS, message)
        server.quit()
        print("Hey the price is good to buy")

    except:
        print('Email failed to send.')

subject = " This is Amazon website: Price is good for buying this PC!"
msg = 'https://www.amazon.com/CYBERPOWERPC-Xtreme-i5-9400F-GeForce-GXiVR8060A8/dp/B07VGJDKZ4/ref=lp_8588813011_1_1?' \
     's=electronics&ie=UTF8&qid=1573003904&sr=1-1' \

check_price()







