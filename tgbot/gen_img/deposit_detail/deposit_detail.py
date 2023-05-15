from PIL import Image, ImageDraw, ImageFont
import textwrap

def split_text_by_width(text, max_width, font_size, font_path):
    image = Image.new("RGB", (1, 1))  # Создаем изображение размером 1x1 пиксель
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    
    lines = []
    current_line = ""
    
    for word in list(text):
        word_width = draw.textsize(word, font=font)[0]
        
        if draw.textsize(current_line + "" + word, font=font)[0] <= max_width:
            current_line += "" + word
        else:
            lines.append(current_line.strip())
            current_line = word
    
    lines.append(current_line.strip())
    
    return lines

def generate_deposit(data):
    deposit = Image.open('tgbot/gen_img/deposit_detail/deposit_detail_start.png')
    
    usdt = Image.open('tgbot/gen_img/deposit_detail/usdt.png')
    tr = Image.open('tgbot/gen_img/deposit_detail/tr.png')
    colon = Image.open('tgbot/gen_img/deposit_detail/colon.png')
    

    #отрисовка времени на телефоне 
    font = ImageFont.truetype('tgbot/gen_img/SFUIText-Semibold.ttf', size=23)
    draw_way = ImageDraw.Draw(deposit)
    draw_way.text(
		(44, 23),
		data['time'],
		font=font,
		fill='#fbfbf9')
    
    # генерация wifi, net, battery
    
    # генерация net
    if data['net'] == '2':
        net = Image.open('tgbot/gen_img/deposit_detail/net_2.png')
    elif data['net'] == '3':
        net = Image.open('tgbot/gen_img/deposit_detail/net_3.png')
    elif data['net'] == '4':
        net = Image.open('tgbot/gen_img/deposit_detail/net_4.png')
        
    deposit.paste(net, (458,27), mask=net.convert('RGBA'))
    
    # генерация wifi
    if data['wifi'] == '1':
        wifi = Image.open('tgbot/gen_img/deposit_detail/wifi_1.png')
    elif data['wifi'] == '2':
        wifi = Image.open('tgbot/gen_img/deposit_detail/wifi_2.png')
    elif data['wifi'] == '3':
        wifi = Image.open('tgbot/gen_img/deposit_detail/wifi_3.png')
        
    deposit.paste(wifi, (492,27), mask=wifi.convert('RGBA'))
    
    # генерация battery
    if data['battery'] == '10':
        battery = Image.open('tgbot/gen_img/deposit_detail/battery_10.png')
    elif data['battery'] == '20':
        battery = Image.open('tgbot/gen_img/deposit_detail/battery_20.png')
    elif data['battery'] == '50':
        battery = Image.open('tgbot/gen_img/deposit_detail/battery_50.png')
    elif data['battery'] == '90':
        battery = Image.open('tgbot/gen_img/deposit_detail/battery_90.png')
        
    deposit.paste(battery, (525,27), mask=battery.convert('RGBA'))
    
    # разбиение даты на элементы
    time_value2 = data['date'].split(' ')
    tm_date = time_value2[0]
    tm_time = time_value2[1]
    
    tm_date = tm_date.split('-')
    tm_time = tm_time.split(':')
    
    # отрисовка разбитой даты
    font = ImageFont.truetype(
    'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(374, 837),
    	tm_date[0],
    	font=font,
    	fill='#e1e4eb')
    deposit.paste(tr, (374+int(font.getsize(tm_date[0])[0])+2, 841), mask=tr.convert('RGBA'))
    font = ImageFont.truetype(
    	'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(374+int(font.getsize(tm_date[0])[0])+10, 837),
    	tm_date[1],
    	font=font,
    	fill='#e1e4eb')
    deposit.paste(tr, (374+int(font.getsize(tm_date[0])[0])+10+int(font.getsize(tm_date[1])[0])+2, 841), mask=tr.convert('RGBA'))
    font = ImageFont.truetype(
    	'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(374+int(font.getsize(tm_date[0])[0])+int(font.getsize(tm_date[1])[0])+20, 837),
    	tm_date[2],
    	font=font,
    	fill='#e1e4eb')
    # new date
    width_for_time = 374+int(font.getsize(tm_date[0])[0])+int(font.getsize(tm_date[1])[0])+int(font.getsize(tm_date[2])[0])+27
    font = ImageFont.truetype(
    	'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(width_for_time, 837),
    	tm_time[0],
    	font=font,
    	fill='#e1e4eb')
    deposit.paste(colon, (width_for_time+int(font.getsize(tm_time[0])[0])+3, 837), mask=colon.convert('RGBA'))
    font = ImageFont.truetype(
    	'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(width_for_time+int(font.getsize(tm_time[0])[0])+9, 837),
    	tm_time[1],
    	font=font,
    	fill='#e1e4eb')
    deposit.paste(colon, (width_for_time+int(font.getsize(tm_time[0])[0])+9+int(font.getsize(tm_time[1])[0])+3, 837), mask=colon.convert('RGBA'))
    font = ImageFont.truetype(
    	'tgbot/gen_img/binance2.ttf', size=16)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(width_for_time+int(font.getsize(tm_time[0])[0])+int(font.getsize(tm_time[1])[0])+18, 837),
    	tm_time[2],
    	font=font,
    	fill='#e1e4eb')
    
    
    
    # отрисовка суммы перевода
    font = ImageFont.truetype('tgbot/gen_img/binance.ttf', size=31)
    draw_lev = ImageDraw.Draw(deposit)
    draw_lev.text(
    	(int(292-((int(font.getsize(data['amount'])[0]) + 8 + 54)/2)), 250),
    	data['amount'],
    	font=font,
    	fill='#e1e4eb')
    
    deposit.paste(usdt, (int(292-((int(font.getsize(data['amount'])[0]) + 8 + 54)/2) + int(font.getsize(data['amount'])[0]) + 10), 254), mask=usdt.convert('RGBA'))

    # draw address
    font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=20)
    lines = split_text_by_width(data['address'],277,20,'tgbot/gen_img/ofont.ru_Roboto.ttf')
    # lines = textwrap.wrap(data['address'], width=23)
    
    start_y = 642
    for line in lines:
        draw_lev = ImageDraw.Draw(deposit)
        draw_lev.text(
            (244 + (277 - int(font.getsize(line)[0])), start_y),
            line,
            font=font,
            fill='#fdffff')
        
        start_y += 28
        
    # draw txid
    font = ImageFont.truetype('tgbot/gen_img/ofont.ru_Roboto.ttf', size=20)
    lines = split_text_by_width(data['txid'],277,20,'tgbot/gen_img/ofont.ru_Roboto.ttf')
    # lines = textwrap.wrap(data['txid'], width=23)
    
    start_y = 727
    for line in lines:
        draw_lev = ImageDraw.Draw(deposit)
        draw_lev.text(
            (244 + (277 - int(font.getsize(line)[0])), start_y),
            line,
            font=font,
            fill='#fdffff')
        draw_lev.line((244 + (277 - int(font.getsize(line)[0])),start_y + 23, 523 ,start_y + 23), fill='#fdffff', width=2)
        start_y += 28
    
    deposit.save(f'tgbot/gen_img/deposit_detail/{data["user_id"]}_output_deposit_detail.png')
     
# net - 2,3,4
# wifi - 1,2,3
# battery - 10,20,50,90
# data = {
#     'time':'20:49',
#     'net':'3',
#     'wifi':'2',
#     'battery':'10',
#     'amount':'29',
#     'network':'TRX',
#     'address':'TTq4GUFGAh2a9VAzabsMfyaqZB8KTd9bim',
#     'txid':'9ece3c91c3d7a3889fe1afebd21fb4c2ce7200ecd28ed54f83971cbd3e5f037f',
#     'date':'2023-04-27 20:41:05',
#     'user_id':'5468686',
# }
    
# generate_deposit(data)