from pprint import pprint #Для более удобного вывода на экран
#product = {
    #'name': 'iPhone 12',
    #'stock': 24,
    #'price': 65432.1
#}
#print(len(product))
#print(product)

#product['memory'] = 256 #Добавляем ключ/значение в словарь
#product['name'] = 'iPhone 12 Pro' #Изменяем ключ/значение в словаре

#print(product['name']) #Обращаемся к элементу по ключу

#print(product.get('discount')) #Метод get возвращает none, если в словаре нет такого ключа. Если есть, то его значение
#print(product.get('discount', 0)) #Возвращает 0 вместо none, либо то что передадим, если такого ключа нет в всловаре

#del product['stock'] #Удаляем ключ
#print(product)

#phones = ["iPhone 12 Pro", "Samsung Galaxy S21", "Xiaomi Mi11"]

#product['recomended'] = phones
#pprint(product)

#pprint(product['recomended'][0]) #Оращаемся к списку и конкретному элементу
#product['recomended'].append('iPhone 9') #Добавляем в список новый элемент
#pprint(product)

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1,
     'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]

#pprint(stock[0]['recomended'])

#stock[0]['recomended'].append('Xiaomi Mi11')

#pprint(stock[0]['recomended'])

pprint(stock[2])

stock[2]['price'] = stock[2]['price'] - 30000
pprint(stock[2])

print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recomended']))