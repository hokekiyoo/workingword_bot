# coding: utf-8
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from bs4 import BeautifulSoup
try:
    from urllib2 import urlopen
except:
    from  urllib.request import urlopen
import re

def FetchWorkingWord():
    #url
    url = "https://www.hatakoto.jp/"
    #get html
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    text = "\n"
    text += soup.find(attrs=["class_","chinContent vertical"]).text
    text += "\n\n"+soup.find(attrs=["class_","chinMsg vertical"]).text
    return text

@respond_to('hello', re.IGNORECASE)
def respondmessage(message):
    text = FetchWorkingWord()
    message.reply(text) 
