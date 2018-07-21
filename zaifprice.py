#coding:utf-8
import requests,json,os.path
from time import sleep
def checktoken():
    if os.path.isfile('token.json'):
        print("APIトークン設定ファイルを確認 \n処理を続行")
    else:
        print("エラー！ \n\
APIトークン設定ファイルの存在を確認できません \n\
設定ファイルを作成します \n\
line_notify_api のAPIトークンを入力してください")

        input_token = input(">>> ")
        print("設定ファイル作成中")
        token_dict = {'line_notify_token':input_token}
        with open('token.json','w') as f:
            json.dump (token_dict,f)
    
        print("設定ファイル作成完了")

def main():
    with open('token.json','r') as f:
        token_dict = json.load(f)
        ACCESS_TOKEN = token_dict['line_notify_token']

    line_notify_api = "https://notify-api.line.me/api/notify"

    while True:

        btc = requests.get('https://api.zaif.jp/api/1/last_price/btc_jpy').json()
        eth = requests.get('https://api.zaif.jp/api/1/last_price/eth_jpy').json()
        xem = requests.get('https://api.zaif.jp/api/1/last_price/xem_jpy').json()
        mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy').json()

    
        payload = {'message': "\n現在のBTCの価格は、" + str(btc['last_price']) + "円です。\n"\
        + "現在のETHの価格は、" + str(eth['last_price']) + "円です。\n"\
        + "現在のXEMの価格は、" + str(xem['last_price']) + "円です。\n"\
        + "現在のmonaの価格は、" + str(mona['last_price']) + "円です。"}
        headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    
        r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)
    
        try:
            r.raise_for_status()
        except:
            print("エラーです！" + str(r))
        else:
            print("success!" + str(r))

        sleep(10)

checktoken()
main()
