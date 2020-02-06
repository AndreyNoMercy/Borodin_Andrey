#number = int(input('Input int 0<: '))
number = 867201
numerals = []

while True:
    if number >= 1:
        n = number % 10
        numerals.append(n)
        number //= 10
    else:
        break

max_n = 0
for i in numerals:
    if i > max_n:
        max_n = i

print(max_n)




