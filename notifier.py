import selenium

import smtplib
from personaldata import *

server = smtplib.SMTP
server.starttls()
server.login(f'{test}')