#coding:utf-8
import requests,zaifapi,json
from time import sleep
from zaifapi import ZaifPublicApi 

while True:

    btc = response = requests.get('https://api.zaif.jp/api/1/last_price/btc_jpy')
    eth = response = requests.get('https://api.zaif.jp/api/1/last_priece/eth_jpy')
    xem = response = requests.get('https://api.zaif.jp/api/1/last_price/xem_jpy')
    mona = response = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy')
    ACCESS_TOKEN = ""   #トークンを入力
    line_notify_api = "https://notify-api.line.me/api/notify"

    payload = {'message': btc}
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}  
    r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)
    try:
        r.raise_for_status()
    except:
        print("エラーです！" + str(r))
    else:
        print("success!" + str(r))

    sleep(10)
