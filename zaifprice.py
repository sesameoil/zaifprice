#coding:utf-8
import requests,json
from time import sleep

ACCESS_TOKEN = ""   #トークンを入力
line_notify_api = "https://notify-api.line.me/api/notify"

while True:

    btc = requests.get('https://api.zaif.jp/api/1/last_price/btc_jpy').json()
    eth = requests.get('https://api.zaif.jp/api/1/last_priece/eth_jpy').json()
    xem = requests.get('https://api.zaif.jp/api/1/last_price/xem_jpy').json()
    mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy').json()

    
    payload = {'message': "現在のBTCの価格は、" + str(btc['last_price']) + "円です。" }
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}  
    
    r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)
    
    try:
        r.raise_for_status()
    except:
        print("エラーです！" + str(r))
    else:
        print("success!" + str(r))

    sleep(10)
