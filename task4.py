string= str(input('Введите несколько слов: '))
print(string)

string_r = string.split(' ')
print(string_r)
i=0
k=1
while i <  len(string_r):
    print(k, string_r[i][0:10])
    i = i + 1
    k = k + 1