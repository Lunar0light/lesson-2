print('Введите 5 элементов списка: ')
a = input()
b = input()
x = input()
c = input()
d = input()
list_1=[a, b, x, c, d]

long = len(list_1)
print('Элементов в списке: ', long)
print(list_1)

el = 0
try:
    while el < long:
        list_1[el], list_1[el+1] = list_1[el+1], list_1[el]
        el = el + 2
except: IndexError

print(list_1)
