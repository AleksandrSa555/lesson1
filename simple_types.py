a = 'Привет'
b = 'мир'
d = 2
c = f'{a} {b} {d}!'
print(c.lower())

e = '    Лента    '
print(e.strip().lower())

f = 'Прив3т т3б3'.replace('3', 'е')
print(f)

g = 'ПриветЫ'.lower().replace('ы', '').capitalize()
print(g)

h ='Привет мир'.replace('мир', 'python')
print(h)

i = 'Предложение из нескольких слов'
print(len(i.split()))

k = None
l = 0
print(k == l)
print(k is None)
print(l is None)