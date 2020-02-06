#Не совсем понял задание, на выполнение ДЗ было выделено фиксирование
#время, поэтому уточнять у Вас не стал и написал 2е версии

#ver. 1, когда мы считаем, что юзер вводит строку
n_1 = str(45)
#n_1 = input('Input int 0 < n < 100:')
nn_1 = n_1 + n_1
nnn_1 = nn_1 + n_1

result_1 = int(n_1) + int(nn_1) + int(nnn_1)

print(result_1)
print()
print('---------------')
print()

#ver. 2, когды мы считаем, юзер вводит число
n_2 = 45
#n_2 = int(input('Input int 0 < n < 100:'))
nn_2 = int(str(n_2) + str(n_2))
nnn_2 = int(str(n_2) + str(nn_2))

result_2 = n_2 + nn_2 + nnn_2
print(result_2)
