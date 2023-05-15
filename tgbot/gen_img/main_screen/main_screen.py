from PIL import Image, ImageDraw, ImageFont
from requests import Request, Session
import json

def get_price(slug):
    # btc 1/ eth 1027/ bnb 1839
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' 
    
    headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '42d7039b-2da8-4791-bcbd-8d2debe9732f'
        }
    if slug == 'bitcoin':

        parameters = { 'slug': slug, 'convert': 'USD' } 
        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        info = json.loads(response.text)
        price = info['data']['1']['quote']['USD']['price']
        change = info['data']['1']['quote']['USD']['percent_change_24h']
        return (price,change)
    
    elif slug == 'ethereum':

        parameters = { 'slug': slug, 'convert': 'USD' } 
        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        info = json.loads(response.text)
        price = info['data']['1027']['quote']['USD']['price']
        change = info['data']['1027']['quote']['USD']['percent_change_24h']
        return (price,change)
    
    elif slug == 'bnb':

        parameters = { 'slug': slug, 'convert': 'USD' } 
        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        info = json.loads(response.text)
        price = info['data']['1839']['quote']['USD']['price']
        change = info['data']['1839']['quote']['USD']['percent_change_24h']
        return (price,change)

def generate_main_screen(data):
    main = Image.open('tgbot/gen_img/main_screen/main_screen_start.png')
    
    price_btc, change_btc = get_price('bitcoin')
    price_bnb, change_bnb = get_price('ethereum')
    price_eth, change_eth = get_price('bnb')

    total_btc =  float(data['total_usdt'].replace(',', '.')) / price_btc
    total_btc = str(round(total_btc,8)).replace('.', ',')

    #отрисовка времени на телефоне 
    font = ImageFont.truetype('tgbot/gen_img/SFUIText-Semibold.ttf', size=23)
    draw_way = ImageDraw.Draw(main)
    draw_way.text(
		(44, 23),
		data['time'],
		font=font,
		fill='#fbfbf9')
    
    # генерация wifi, net, battery
    
    # генерация net
    if data['net'] == '2':
        net = Image.open('tgbot/gen_img/main_screen/net_2.png')
    elif data['net'] == '3':
        net = Image.open('tgbot/gen_img/main_screen/net_3.png')
    elif data['net'] == '4':
        net = Image.open('tgbot/gen_img/main_screen/net_4.png')
        
    main.paste(net, (458,27), mask=net.convert('RGBA'))
    
    # генерация wifi
    if data['wifi'] == '1':
        wifi = Image.open('tgbot/gen_img/main_screen/wifi_1.png')
    elif data['wifi'] == '2':
        wifi = Image.open('tgbot/gen_img/main_screen/wifi_2.png')
    elif data['wifi'] == '3':
        wifi = Image.open('tgbot/gen_img/main_screen/wifi_3.png')
        
    main.paste(wifi, (492,27), mask=wifi.convert('RGBA'))
    
    # генерация battery
    if data['battery'] == '10':
        battery = Image.open('tgbot/gen_img/main_screen/battery_10.png')
    elif data['battery'] == '20':
        battery = Image.open('tgbot/gen_img/main_screen/battery_20.png')
    elif data['battery'] == '50':
        battery = Image.open('tgbot/gen_img/main_screen/battery_50.png')
    elif data['battery'] == '90':
        battery = Image.open('tgbot/gen_img/main_screen/battery_90.png')
        
    main.paste(battery, (525,27), mask=battery.convert('RGBA'))
    
    # отрисовка баланса
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=32)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (22, 228),
        total_btc,
        font=font,
        fill='#f7f8ff')
    
    data['total_usdt'] = data['total_usdt'] + '$'
    font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (41, 275),
        data['total_usdt'],
        font=font,
        fill='#666b76')
    
    
    # отрисовк апрямоугольников для изменения цены за 24ч

    draw_lev = ImageDraw.Draw(main)
    if change_bnb <= 0:
        draw_lev.rounded_rectangle((443,872,567,926),radius=5, fill='#d6475e')
    else:
        draw_lev.rounded_rectangle((443,872,567,926),radius=5, fill='#71bd88')
        
    if change_btc <= 0:
        draw_lev.rounded_rectangle((443,962,567,1016),radius=5, fill='#d6475e')
    else:
        draw_lev.rounded_rectangle((443,962,567,1016),radius=5, fill='#71bd88')
        
    if change_eth <= 0:
        draw_lev.rounded_rectangle((443,1052,567,1106),radius=5, fill='#d6475e')
    else:
        draw_lev.rounded_rectangle((443,1052,567,1106),radius=5, fill='#71bd88')


    if change_bnb <= 0:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (471, 882),
            '-',
            font=font,
            fill='#f7f8ff')
    else:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (468, 882),
            '+',
            font=font,
            fill='#f7f8ff')
    font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (525, 884),
        '%',
        font=font,
        fill='#f7f8ff')
        
    if change_btc <= 0:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (471, 972),
            '-',
            font=font,
            fill='#f7f8ff')
    else:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (468, 973),
            '+',
            font=font,
            fill='#f7f8ff')
    font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (525, 973),
        '%',
        font=font,
        fill='#f7f8ff')
        
    if change_eth <= 0:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (471, 1062),
            '-',
            font=font,
            fill='#f7f8ff')
    else:
        font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
        draw_lev = ImageDraw.Draw(main)
        draw_lev.text(
            (468, 1063),
            '+',
            font=font,
            fill='#f7f8ff')
    font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=22)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (525, 1062),
        '%',
        font=font,
        fill='#f7f8ff')
    
    # отрисовка change_bnb
    change_bnb = str(change_bnb).replace('.',',')
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=16)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (480, 895),
        change_bnb[:4],
        font=font,
        fill='#f7f8ff')
    
    # отрисовка change_btc
    change_btc = str(change_btc).replace('.',',')
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=16)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (480, 984),
        change_btc[:4],
        font=font,
        fill='#f7f8ff')
    
    # отрисовка change_eth
    change_eth = str(change_eth).replace('.',',')
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=16)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (480, 1073),
        change_eth[:4],
        font=font,
        fill='#f7f8ff')
    
    # отрисовка последней цены
    # price_btc, change_btc = get_price('bitcoin')
    # price_bnb, change_bnb = get_price('ethereum')
    # price_eth, change_eth = get_price('bnb')
    
    
    price_bnb = round(price_bnb,2)
    price_bnb = str(price_bnb).replace('.',',')
    
    if len(price_bnb.split(',')[0]) == 4:
       price_bnb = price_bnb[0] + ' ' + price_bnb[1:]
    elif len(price_bnb.split(',')[0]) == 5:
       price_bnb = price_bnb[0] + price_bnb[1] + ' ' + price_bnb[2:]
    
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=18)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (398 - int(font.getsize(price_bnb)[0]), 881),
        price_bnb,
        font=font,
        fill='#f7f8ff')
    
    price_bnb = price_bnb + '$'
    font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (402 - int(font.getsize(price_bnb)[0]), 916),
        price_bnb,
        font=font,
        fill='#666b76')
    
    
    price_btc = round(price_btc,2)
    price_btc = str(price_btc).replace('.',',')
    
    if len(price_btc.split(',')[0]) == 4:
       price_btc = price_btc[0] + ' ' + price_btc[1:]
    elif len(price_btc.split(',')[0]) == 5:
       price_btc = price_btc[0] + price_btc[1] + ' ' + price_btc[2:]
    
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=18)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (398 - int(font.getsize(price_btc)[0]), 970),
        price_btc,
        font=font,
        fill='#f7f8ff')
    
    price_btc = price_btc + '$'
    font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (402 - int(font.getsize(price_btc)[0]), 1005),
        price_btc,
        font=font,
        fill='#666b76')
    
    
    price_eth = round(price_eth,2)
    price_eth = str(price_eth).replace('.',',')
    
    if len(price_eth.split(',')[0]) == 4:
       price_eth = price_eth[0] + ' ' + price_eth[1:]
    elif len(price_eth.split(',')[0]) == 5:
       price_eth = price_eth[0] + price_eth[1] + ' ' + price_eth[2:]
    
    
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=18)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (398 - int(font.getsize(price_eth)[0]), 1059),
        price_eth,
        font=font,
        fill='#f7f8ff')
    
    price_eth = price_eth + '$'
    font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
    draw_lev = ImageDraw.Draw(main)
    draw_lev.text(
        (402 - int(font.getsize(price_eth)[0]), 1094),
        price_eth,
        font=font,
        fill='#666b76')
    
    

    main.save(f'tgbot/gen_img/main_screen/{data["user_id"]}_output_main_screen.png')
    
# net - 2,3,4
# wifi - 1,2,3
# battery - 10,20,50,90
# data = {
#     'time':'12:49',
#     'net':'4',
#     'wifi':'3',
#     'battery':'50',
#     'total_usdt' : '1352,22',
#     'user_id':'5468686',
# }
    
# generate_main_screen(data)    
    
    
# print(get_price('bitcoin'))
# print(get_price('ethereum'))
# print(get_price('bnb'))