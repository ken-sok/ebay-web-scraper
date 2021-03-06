#library to for webscraping
import requests
#library to parse 
from bs4 import BeautifulSoup
#smtp
import smtplib

URL = 'https://www.ebay.com/itm/Sony-Xperia-XA2-H3123-5-2-32GB-4G-LTE-Factory-GSM-Unlocked-Smartphone/163158951964'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def check_price(): 

    #return data from website
    page = requests.get(URL, headers=headers)

    #parse the page
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="itemTitle")
    print(''.join(text for text in title.find_all(text=True)
                if text.parent.name != "span"))

    price = soup.find("span", {"itemprop": "price", "content": True})['content']
    print("$", price)
    price = float(price)
    if (price < 160): 
        send_mail()

def send_mail():
    
    #using gmail smtp
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    #establish connection between email server
    server.ehlo()
    #encrypt
    server.starttls()
    
    server.ehlo()
    server.login('<gmail mail>', '<input password>')

    subject = "Price fell down!"
    body = "Check the ebay link: " + URL


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '<sender email>',
        '<recipient email>',
        msg
    )

    print('EMAIL SENT!')
    server.quit()

#call funtion
check_price()
