# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import email
import smtplib

# <codecell>

from email.mime.text import MIMEText

# <codecell>

lic = open('LICENSE', 'rb')

# <codecell>

msg = MIMEText(lic.read())

# <codecell>

lic.close()

# <codecell>

msg['Subject'] = 'The contents of %s' % msg

# <codecell>

msg['From'] = ('will@artcontrol.me')

# <codecell>

msg['To'] = ('peter@brobeur.com')

# <codecell>

s = smtplib.SMTP('localhost')

# <codecell>

s.sendmail('will@artcontrol.me', [you], msg.as_string())
s.quit()

# <codecell>

ps = open('ps', 'r')

# <codecell>

passW = ps.readline()

# <codecell>


# <codecell>


# <codecell>

#!/usr/bin/python -tt

from email.mime.text import MIMEText
from datetime import date
import smtplib

SMTP_SERVER = ("smtpout.secureserver.net")
SMTP_PORT = 80
SMTP_USERNAME = ("will@artcontrol.me")
SMTP_PASSWORD = passW

EMAIL_TO = (["peter@brobeur.com"])
EMAIL_FROM = ("will@gmail.com")
EMAIL_SUBJECT = ("Demo Email : ")

DATE_FORMAT = ("%d/%m/%Y")
EMAIL_SPACE = (", ")

DATA=('This is the content of the email.')

def send_email():
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + (" %s") % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()

# <codecell>

import string
import sys
from email.MIMEText import MIMEText

# <codecell>

readfile = 'README.md'
f = file(readfile)
attach = MIMEText(f.read())
attach.add_header('Content-Disosition', 'attachment', filename=readfile)

# <codecell>

import smtplib  
      
fromz = 'hamnmersmake@gmail.com'  
toz = 'will@artcontrol.me'  
msg = 'Peter is drinking tea! '  
      
      
# Credentials (if needed)  
username = 'hammersmake@gmail.com'
password = passW   
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromz, toz, msg)  

# <codecell>

subject = ('Good Morning!')

# <codecell>

nums = 1

# <codecell>

for nums in range(2):
    import smtplib  
      
    fromz = 'hamnmersmake@gmail.com'  
    toz = 'will@artcontrol.me'  
    msg = 'Fez is sitting on couch!'  
      
      
    # Credentials (if needed)  
    username = 'hammersmake@gmail.com'
    password = passW   
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromz, toz, msg)  

# <codecell>

li = [i.strip().split() for i in open("emz").readlines()]

# <codecell>

newListz = []

# <codecell>

print newListz

# <codecell>

newListz.append(li)

# <codecell>

print newListz

# <codecell>

print li

# <codecell>

emailist = list(li)

# <codecell>

print emailist

# <codecell>

print emailist.sort()

# <codecell>

i.close('emz')

# <codecell>

body = ('This is all the text in the world!')

# <codecell>

emilz = string.join((
    'From %s' % fromz,
    'To: %s' % toz, 
    'Subject: %s' % subject,
    "",
    body), '\r\n')

# <codecell>

server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromz, [toz], emilz)  

# <codecell>

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
 
msg = MIMEMultipart()
msg['Subject'] = ('Email From Python jajaja')
msg['From'] = ('hammersmake@gmail.com')
msg['To'] = ('hammersmake@gmail.com')
 
# That is what u see if dont have an email reader:
msg.preamble = 'Multipart massage.\n'
 
# This is the textual part:
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)
 
# This is the binary part(The Attachment):
part = MIMEApplication(open("README.md","rb").read())
part.add_header('Content-Disposition', 'attachment', filename="README.md")
msg.attach(part)
 
# Create an instance in SMTP server
smtp = SMTP("smtp.gmail.com:587")
# Start the server:
smtp.login("hammersmake@gmail.com", passW)
# Send the email
smtp.sendmail(msg['From'], msg['To'], msg.as_string())

# <codecell>


# <codecell>


