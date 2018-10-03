import discord # インストールした discord.py
import requests
from bs4 import BeautifulSoup
import random

url="https://jp.leagueoflegends.com/ja/news/game-updates/patch"
lolurl="https://jp.leagueoflegends.com"


happy=["motio009","Ryoki4013","taka56","yumay","yuya029","MaoooN","ふーキーん"]
client = discord.Client()
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('/lol'):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        tag=soup.select("body > div.section-wrapper.section-wrapper-primary > div.section-wrapper-content > div > div > div > div > div > div > div.views-row.views-row-1.views-row-odd.views-row-first > div > div > div > div > div.default-2-3 > h4 > a")
        href=tag[0].attrs["href"]
        patch=lolurl+href
        await client.send_message(message.channel, patch)
        r = requests.get(patch)
        soup = BeautifulSoup(r.text, 'lxml')
        div=soup.find_all("div", class_="patch-change-block white-stone accent-before")
        if len(div) > 0:
            for i in range(len(div)):
                champname=div[i].h3.string
                sumarry=div[i].p.string
                note=champname+"\n"+"    "+sumarry
                if i==0:
                    all=note
                elif i>0:
                    all=all+"\n"+note
        await client.send_message(message.channel, all)

    if message.content.startswith('/choice'):
        choice=random.choice(happy)
        await client.send_message(message.channel, choice)

client.run('NDk0ODIxNDExNzIzMTQ5MzIy.Do5HLA.MSJStDbBUW5RJEMZ_Tsff3sheIA')
