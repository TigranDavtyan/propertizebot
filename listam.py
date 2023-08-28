import asyncio
from loader import db
import requests
from random import random
import re
from datetime import datetime, timedelta
import time
import random

USER_AGENTS = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/116.0'
'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.2.765 Yowser/2.5 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
]

#robert_arsenyan%40mail.ru
#Robo1998

login_url = 'https://www.list.am/login'
login_body = "phone_number_or_email={login}&password={password}&timestamp=e8f1a0a1d7232e21012a0e0b149afb35&_form_action=Login&form0_form_visited=1"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,hy;q=0.8",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
itemid_date = re.compile(r'Next renewal<br>(.+?)\"><?/?d?i?v?>?<a href=\"/edit/([0-9]+?)\" title=\"Edit\">')
renewable_listings = re.compile(r"""onclick=\"renew\('(\d+?)'\)""")

class User:
    users = {}
    @classmethod
    def get(cls, cid):
        if cid not in cls.users:
            return cls(cid)
        return cls.users[cid]

    def __init__(self, cid):
        self.cid = cid
        self.session = requests.session()
        self.login_body = login_body
        self.headers = headers
        self.headers['user_agent'] = USER_AGENTS[0]
        self.nRenews = 0
        self.nErrors = 0
        self.latestRenew = None
        User.users[cid] = self

    def login(self):
        phone, email, password = db.fetchone('SELECT phone_number, email, password FROM users WHERE cid = ?;', (self.cid,))
        login = phone if phone else email
        
        self.login_body = self.login_body.format(login=login, password = password)

        res = self.session.post(login_url, self.login_body, headers = self.headers)
        self.session.close()
        return res.status_code

    def getMyListings(self):
        res = self.session.get('https://www.list.am/en/my', headers = self.headers)
        if res.status_code == 200:
            return res.content.decode('utf-8')
        else:
            res = self.login()
            if res != 200:
                return res
            res = self.session.get('https://www.list.am/en/my', headers = self.headers)
            if res.status_code == 200:
                return res.content.decode('utf-8')
            else: 
                return res.status_code
        
            
    def renewListing(self, itemid):
        data = {
            '_form_action': 'Renew',  # Action to renew the listing
            'form0_form_visited': '1',  # Required form field
            'Renew': 'Renew',  # The button value to renew
        }
        res = self.session.post(f'https://www.list.am/my?w=7&i={itemid}', data=data, headers = self.headers)
        return res.status_code
    async def sleep(self):
        await asyncio.sleep(random.random() + 0.8)
    
    async def renewListings(self):
        if self.latestRenew and datetime.now() - self.latestRenew < timedelta(minutes=30):
            return -1
        
        self.login()
        page = self.getMyListings()
        await self.sleep()

        if type(page) == int:
            raise ValueError(f'Cant get {self.cid} users listings. Status code {page}')
        
        items = renewable_listings.findall(page)
        for item in items:
            res = self.renewListing(item)
            await self.sleep()
            if res == 200:
                self.nRenews += 1
            else:
                self.nErrors += 1

        self.latestRenew = datetime.now()
        self.session.close()
        return 0