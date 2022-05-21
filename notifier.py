from selenium import webdriver
import time

import smtplib
from personaldata import *

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(emailaddress, emailpassword)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(emailaddress, emailaddress, message)
        server.quit()
        print("Email sent.")
    except:
        print("Email failed to send.")

PATH = "C:\Windows\System32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://guts.events/m3pgrw/f215lz/resale")

for i in range(100000):
    time.sleep(5)
    page = driver.page_source
    word = "Vrijdag"
    if (word in page) == True:
        print("Ticket gevonden!")
        send_email('Ticket gevonden!', 'Er is een ticket gevonden voor vrijdag!')
    else:
        print('[]')
    driver.refresh()

driver.quit()