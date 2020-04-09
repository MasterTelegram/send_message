# -*- coding: utf-8 -*-
from telethon import utils
import socks
import time
from telethon import TelegramClient, events, sync
import json
### --------------------------------------------------------------------------
print ('[+] Программа поиска сообщений')
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest

ip           = '196.18.3.55'
port         = 8000
password     = 'Fkv7JY'
userproxy    = 'YHB8GP'
api_hash     = '1b40d1d01f8922b384d44e29d32f6acf'
api_id       = 192804
phone_number = '+79228418088'
client = TelegramClient('session_'+str(phone_number),api_id=api_id,api_hash=api_hash,proxy=(socks.HTTP,ip,port,'',password,userproxy))
client.connect()    

tip  = ''
lim  = 0
tp   = 0
sl   = 0

#import pymysql
#db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
#cursor = db.cursor()
#sql = "INSERT INTO send_info (`tip`,`lim_s`,`sl`,`tp`) VALUES ('{}',{},{},{})".format (tip,lim_s,tp,sl)
#cursor.execute(sql)
#db.commit()

if not client.is_user_authorized():
    print ('[+] Нет клиента')
else:
    print ('[+] Версия 3.8')
message = 'Начало работы'
client.send_message(1402034717, message)

@client.on(events.NewMessage)
async def my_event_handler(event):
    print ('[+] Новое сообщение')
    message = str(event)
    if message.find ('channel_id=1402034717') != -1:
        message_in   = str(event)
        message_text = event.message.message

        
        message_text = message_text.replace("stop","stop ")

        message_text = message_text.replace("  "," ")
        list = message_text.split(' ')

        print ('[+1]',list)

        channel_username = '1402034717'        
        tip     = ''
        lim_s   = 0
        tp      = 0
        sl      = 0
        print ('[t] 1:{}, 2:{}, 3:{}, 4:{}, 5:{}'.format(list[0],list[1],list[2],list[4],list[6]))
        instrum = list[0]
        tip     = list[1]
        lim     = float(list[2].replace(",","."))
        tp      = float(list[4].replace(",","."))
        sl      = float(list[6].replace(",","."))
        print ('[+ d] 1:{}, 2:{}, 3:{}, 4:{}, 5:{}'.format(instrum,tip,lim,tp,sl))
        import pymysql
        db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
        cursor = db.cursor()
        sql = "INSERT INTO send_info (`instrum`,`tip`,`lim`,`sl`,`tp`) VALUES ('{}','{}',{},{},{})".format (instrum,tip,lim,tp,sl)
        print ('[sql]',sql)
        cursor.execute(sql)
        db.commit()        
        await client.send_message(1402034717, 'Отправлено ...')
        print ('[+] message')




client.start()
client.run_until_disconnected()













