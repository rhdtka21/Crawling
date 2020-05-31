import time
from bs4 import BeautifulSoup
import telegram
import requests
import os

LOLALARMCHANNEL = ---your_telegram_channel_code---
bot = telegram.Bot(token='---your_telegram_token---')
hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}

url = 'https://www.op.gg/champion/statistics'
req = requests.get(url, headers=hdr)
html = req.text
s = BeautifulSoup(html, 'html.parser')
message = ''
for lane in ['TOP', 'JUNGLE', 'MID', 'ADC', 'SUPPORT']:
    message = lane + ' 상위 5 챔피언\n'
    soup = s.find("div", {"class" : "detail-ranking__content detail-ranking__content--champ-list ChampionRankingList-WinRatio-{} tabItem".format(lane)})
    names = soup.find_all("div", {"class" : "champion-ratio__name"})[:5]
    infos = soup.find_all("div", {"class" : "champion-ratio__percent"})[:10]
    for idx in range(5):
        message += (str(idx+1) + '. ' + names[idx].text.strip() + '\n')
        message += ('   ' + infos[2*idx].text.strip().replace('\n', ' ') + ' ' + infos[2*idx+1].text.strip().replace('\n', ' ')) + '\n'
    message += '\n'
    bot.sendMessage(LOLALARMCHANNEL, message)
