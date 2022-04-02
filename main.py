from lib2to3.pgen2 import driver
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from telethon import TelegramClient, events, hints
from telethon.tl.functions.messages import SendMessageRequest
api_id = 8759328
api_hash = '1a270788cb618993f54f514f5a8c93c4'
client = TelegramClient('admin', api_id, api_hash)
async def main():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.headless = True
    driver = webdriver.Chrome(chrome_options=chrome_option)
    while True:
        crawl = requests.get('https://cryptopanic.com/api/v1/posts/?auth_token=84fac65e9e2f153b086c6abeede45fb9beff45f9').json()
        crawl = crawl['results']
        for i in range(0,20,1):
            try:
                title = crawl[i]['title']
                driver.get(crawl[i]['url'])
                time.sleep(30)
                content = driver.find_element_by_class_name('description-body').text
                string = title + '\n\n' + content
                await client(SendMessageRequest('t.me/autotoolvn',string))
            except:
                pass
with client:
    client.loop.run_until_complete(main())







    