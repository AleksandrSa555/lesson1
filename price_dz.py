def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

get_price= format_price(56.24)
print(get_price)