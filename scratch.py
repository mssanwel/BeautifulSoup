import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.com/G-Shock-Combi-Military-Watch-Black/dp/B003WPUU0U/ref=cts_wa_1_vtp'
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

page=requests.get(URL, headers=headers)
#soup=BeautifulSoup(page.content, 'html.parser')
#price = soup.find(id = "productTitle")
soup = BeautifulSoup(page.content, 'html.parser')

soup1 = BeautifulSoup(soup.prettify(), "html.parser")

title = soup1.find(id="productTitle")

print(title)

server=smtplib.SMTP("smtp.gmail.com", 587)
#server.ehlo()
server.starttls()

#server.ehlo()

server.login("anwelbusiness@gmail.com", 'iupnlqwvvopnmnhu')
server.sendmail('anwelbusiness@gmail.com','saadanwel@hotmail.com', "testing")
print('email sent')

server.quit()




#headers = {'Cache-Control': 'no-cache', "Pragma": "no-cache"}