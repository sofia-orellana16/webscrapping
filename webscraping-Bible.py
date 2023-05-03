import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapters = list(range(1,22))
randomizer = random.choice(chapters)


if randomizer < 10:
    randomizer = '0'+str(randomizer)
else:
    randomizer = str(randomizer)

webpage = 'https://ebible.org/asv/JHN'+randomizer+'.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

verses = soup.findAll('div', class_='main')

for verse in verses:
    verse_list = verse.text.split('.')

mychoice = random.choice(verse_list[:-5])

verse_choice = 'Chapter:', randomizer, 'Verse:', mychoice

print(verse_choice)

import keys
from twilio.rest import Client

Twilionumber = '+12148335896'

mycellphone = '+12542142839'

textmessage = Client.messages.create(to=mycellphone, from_=Twilionumber, 
                                     body=verse_choice)