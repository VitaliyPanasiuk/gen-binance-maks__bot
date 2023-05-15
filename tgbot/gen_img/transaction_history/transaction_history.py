from PIL import Image, ImageDraw, ImageFont


def generate_transaction_history(data):
    history = Image.open('tgbot/gen_img/transaction_history/transaction_history_start.png')
    
    tr = Image.open('tgbot/gen_img/transaction_history/tr.png')
    colon = Image.open('tgbot/gen_img/transaction_history/colon.png')
    
    

    #отрисовка времени на телефоне 
    font = ImageFont.truetype('tgbot/gen_img/SFUIText-Semibold.ttf', size=23)
    draw_way = ImageDraw.Draw(history)
    draw_way.text(
		(44, 23),
		data['time'],
		font=font,
		fill='#fbfbf9')
    
    # генерация wifi, net, battery
    
    # генерация net
    if data['net'] == '2':
        net = Image.open('tgbot/gen_img/transaction_history/net_2.png')
    elif data['net'] == '3':
        net = Image.open('tgbot/gen_img/transaction_history/net_3.png')
    elif data['net'] == '4':
        net = Image.open('tgbot/gen_img/transaction_history/net_4.png')
        
    history.paste(net, (458,27), mask=net.convert('RGBA'))
    
    # генерация wifi
    if data['wifi'] == '1':
        wifi = Image.open('tgbot/gen_img/transaction_history/wifi_1.png')
    elif data['wifi'] == '2':
        wifi = Image.open('tgbot/gen_img/transaction_history/wifi_2.png')
    elif data['wifi'] == '3':
        wifi = Image.open('tgbot/gen_img/transaction_history/wifi_3.png')
        
    history.paste(wifi, (492,27), mask=wifi.convert('RGBA'))
    
    # генерация battery
    if data['battery'] == '10':
        battery = Image.open('tgbot/gen_img/transaction_history/battery_10.png')
    elif data['battery'] == '20':
        battery = Image.open('tgbot/gen_img/transaction_history/battery_20.png')
    elif data['battery'] == '50':
        battery = Image.open('tgbot/gen_img/transaction_history/battery_50.png')
    elif data['battery'] == '90':
        battery = Image.open('tgbot/gen_img/transaction_history/battery_90.png')
        
    history.paste(battery, (525,27), mask=battery.convert('RGBA'))
    
    # отрисовка всех блоков транзакций
    deposit_icon = Image.open('tgbot/gen_img/transaction_history/deposit_icon.png')
    transfer = Image.open('tgbot/gen_img/transaction_history/transfer_icon.png')
    withdraw = Image.open('tgbot/gen_img/transaction_history/withdraw_icon.png')
    arrow = Image.open('tgbot/gen_img/transaction_history/arrow_icon.png')
    
    plus = Image.open('tgbot/gen_img/transaction_history/plus_icon.png')
    minus = Image.open('tgbot/gen_img/transaction_history/minus_icon.png')
    
    start_y = 284
    for tran in data['list_of_transactions']:
        if tran[0] == 'deposit':
            history.paste(deposit_icon, (22,start_y), mask=deposit_icon.convert('RGBA'))
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=23)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 3),
                'Deposit',
                font=font,
                fill='#eff4fc')
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=20)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 40),
                tran[1],
                font=font,
                fill='#858992')
            
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 76),
                tran[2],
                font=font,
                fill='#858992')
            history.paste(arrow, (553, start_y + 72), mask=arrow.convert('RGBA'))
            
            
            history.paste(plus, (566 - int(font.getsize(tran[3])[0]) - 28, start_y + 15), mask=plus.convert('RGBA'))
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=18)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (566 - int(font.getsize(tran[3])[0]), start_y + 14),
                tran[3],
                font=font,
                fill='#69ac89')
            
        elif tran[0] == 'withdraw':
            history.paste(withdraw, (22,start_y), mask=withdraw.convert('RGBA'))
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=23)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 3),
                'Withdraw',
                font=font,
                fill='#eff4fc')
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=20)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 40),
                tran[1],
                font=font,
                fill='#858992')
            
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 76),
                tran[2],
                font=font,
                fill='#858992')
            history.paste(arrow, (553, start_y + 72), mask=arrow.convert('RGBA'))
            
            history.paste(minus, (566 - int(font.getsize(tran[3])[0]) - 23, start_y + 20), mask=minus.convert('RGBA'))
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=18)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (566 - int(font.getsize(tran[3])[0]), start_y + 14),
                tran[3],
                font=font,
                fill='#b5556f')
            
        elif tran[0] == 'transfer':
            history.paste(transfer, (22,start_y), mask=transfer.convert('RGBA'))
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=23)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 3),
                'Transfer',
                font=font,
                fill='#eff4fc')
            
            font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=20)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 40),
                tran[1],
                font=font,
                fill='#858992')
            
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=14)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (90, start_y + 76),
                tran[2],
                font=font,
                fill='#858992')
            
            history.paste(minus, (566 - int(font.getsize(tran[3])[0]) - 23, start_y + 20), mask=minus.convert('RGBA'))
            font = ImageFont.truetype('tgbot/gen_img/binance2.ttf', size=18)
            draw_lev = ImageDraw.Draw(history)
            draw_lev.text(
                (566 - int(font.getsize(tran[3])[0]), start_y + 14),
                tran[3],
                font=font,
                fill='#b5556f')
        start_y += 146
            
    
    
    
    history.save(f'tgbot/gen_img/transaction_history/{data["user_id"]}_output_transaction_history.png')
    
    
# net - 2,3,4
# wifi - 1,2,3
# battery - 10,20,50,90
# data = {
#     'time':'20:49',
#     'net':'4',
#     'wifi':'1',
#     'battery':'50',
#     'list_of_transactions':[['deposit','Crypto','2023-04-27 20:41:05','90,00'],['withdraw','Crypto','2023-04-27 20:24:37','120,00'],['withdraw','Crypto','2023-04-27 20:24:37','19,00'],['transfer','Funding Wallet','2023-04-27 10:42:37','200,00']],
#     'user_id':'5468686',
# }
    
# generate_transaction_history(data)