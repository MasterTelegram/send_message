# -*- coding: utf-8 -*-
import asyncio
import websockets
import json
import iz_func
import time

print ('[+] v 1.2')

async def sell(name,sec_key,lim_s,lim_b,tp,sl):
    uri  = "wss://wsbot.viking.trade:17799/"
    async with websockets.connect(uri) as websocket:
        print ('')
        print (iz_func.c2+'[+] Авторизация',iz_func.c23)
        message_out = ""
        api_key = "nDO8fJouoEPhcTSEwBuC1CslaaV2zJgLrX8uYWhYog8F0Dz7iVGsdYETZH7E9OWwAEVrT3xmBMdZols3"
        email   = 'vikingtrade.io@gmail.com'
        api_key = "R2IyWB0TRdTiyrZhkj5qbkqwOXtnCoIwqej5VR0uD0xlymlHW0tWtfQTCTursbFra08y4taavaCA1W3B"
        email   = 'tm91tb@yandex.ru'        
        message_out = '{"type":"authorization_key", "data":{"key":"nDO8fJouoEPhcTSEwBuC1CslaaV2zJgLrX8uYWhYog8F0Dz7iVGsdYETZH7E9OWwAEVrT3xmBMdZols3","email":"vikingtrade.io@gmail.com"}}'
        response = json.loads(message_out)
        await websocket.send(message_out)
        print("Запрос:",message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting)

        print ('[+] Только br6sell и re_sell') 
        print ('')
        print ('') 
        print ('[+] 3. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"sec_field", "data":{"robot_id":"10", "name":"'+name+'", "sname":"'+str(sec_key)+'", "security":{"sl":'+str(sl)+', "tp": '+str(tp)+'}}}'
        print("Запрос:",message_out)
        response = json.loads(message_out)
        await websocket.send(message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 

        print ('')
        print ('') 
        print ('[+] 2. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"portfolio_field","data":{"robot_id":"10","name":"'+name+'","f_name":"lim_s" ,"f_value":'+str(lim_s)+'}}'
        print("Запрос:",message_out)
        response = json.loads(message_out)
        await websocket.send(message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 

        print ('')
        print ('[+] ') 
        print ('[+] 1. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"portfolio_field","data":{"robot_id":"10","name":"'+name+'","f_name":"re_sell" ,"f_value":true}}'
        response = json.loads(message_out)
        await websocket.send(message_out)
        print("Запрос:",message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 


async def buy(name,sec_key,lim_s,lim_b,tp,sl):
    uri  = "wss://wsbot.viking.trade:17799/"
    async with websockets.connect(uri) as websocket:
        print ('')
        print (iz_func.c2+'[+] Авторизация',iz_func.c23)
        message_out = ""
        api_key = "nDO8fJouoEPhcTSEwBuC1CslaaV2zJgLrX8uYWhYog8F0Dz7iVGsdYETZH7E9OWwAEVrT3xmBMdZols3"
        email   = 'vikingtrade.io@gmail.com'
        api_key = "R2IyWB0TRdTiyrZhkj5qbkqwOXtnCoIwqej5VR0uD0xlymlHW0tWtfQTCTursbFra08y4taavaCA1W3B"
        email   = 'tm91tb@yandex.ru'        
        message_out = '{"type":"authorization_key", "data":{"key":"nDO8fJouoEPhcTSEwBuC1CslaaV2zJgLrX8uYWhYog8F0Dz7iVGsdYETZH7E9OWwAEVrT3xmBMdZols3","email":"vikingtrade.io@gmail.com"}}'
        response = json.loads(message_out)
        await websocket.send(message_out)
        print("Запрос:",message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting)

        print ('[+] Только buy') 
        print ('')
        print ('') 
        print ('[+] 3. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"sec_field", "data":{"robot_id":"10", "name":"'+name+'", "sname":"'+str(sec_key)+'", "security":{"sl":'+str(sl)+', "tp": '+str(tp)+'}}}'
        print("Запрос:",message_out)
        response = json.loads(message_out)
        await websocket.send(message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 

        print ('')
        print ('') 
        print ('[+] 2. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"portfolio_field","data":{"robot_id":"10","name":"'+name+'","f_name":"lim_b" ,"f_value":'+str(lim_b)+'}}'
        print("Запрос:",message_out)
        response = json.loads(message_out)
        await websocket.send(message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 

        print ('')
        print ('[+] ') 
        print ('[+] 1. Отправить запросы на изменения параметров портфеля и инструмента')
        message_out = '{"type":"portfolio_field","data":{"robot_id":"10","name":"'+name+'","f_name":"re_buy" ,"f_value":true}}'
        response = json.loads(message_out)
        await websocket.send(message_out)
        print("Запрос:",message_out)
        greeting = await websocket.recv()
        print("Ответ:",greeting) 


while 1==1:
    import pymysql
    db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    cursor = db.cursor()
    sql = "select id,tip,lim,tp,sl,instrum,end from send_info where end <> 'no';"
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data: 
        id,tip,lim,tp,sl,instrum,end = rec
        lastid = id
        print ('[+] {}, tip:{} lim:{} 2:{} 3:{} 4:{} 5:{}'.format(id,tip,lim,tp,sl,instrum,end))

        if tip == "продали":
            # BR продали 50,43 stop 50,64  profit 49,86
            if instrum == 'Si':
                name = 'si6sell' 
                sec_key = "SiM0"

            if instrum == 'BR':
                name = 'br6sell'
                sec_key = "BRK0"

            if instrum == 'RTS':
                name = 'rts6sell'
                sec_key = "RIM0"

            if instrum == 'GOLD':
                name = 'gd6sell'
                sec_key = "GDM0"

            lim_s        = lim
            lim_b        = 0
            sl           = sl - lim
            tp           = lim - tp


            print ('[=] instrum {} sl:{} {}'.format(instrum,sl,tp)) 

            asyncio.get_event_loop().run_until_complete(sell(name,sec_key,lim_s,lim_b,tp,sl))

        if tip == "купили":
            #BR купили 59,15  stop 58,79  profit 59,51

            if instrum == 'Si':
                name = 'si6buy'
                sec_key = "SiM0"

            if instrum == 'BR':
                name = 'br6buy'
                sec_key = "BRK0"

            if instrum == 'RTS':
                name = 'rts6buy'
                sec_key = "RIM0"

            if instrum == 'GOLD':
                name = 'gd6buy'
                sec_key = "GDM0"

            lim_s        = 0        
            lim_b        = lim         
            sl           = lim - sl 
            tp           = tp - lim
            asyncio.get_event_loop().run_until_complete(buy(name,sec_key,lim_s,lim_b,tp,sl))


        sql = "UPDATE send_info SET end = 'no' WHERE `id` = "+str(lastid)+""
        cursor.execute(sql)
        db.commit()
    print ('[+] Ожидание ...')
    time.sleep (5)