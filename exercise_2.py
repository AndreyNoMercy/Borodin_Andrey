#time_in_sec = int(input('Время в секундах: '))
time_in_sec = 9876

time_in_min = time_in_sec / 60
time_in_h = time_in_min / 60

min_out_h = (time_in_h - int(time_in_h)) * 60
sec_out_min = round((min_out_h - int(min_out_h)) * 60)

print(f"{int(time_in_h)}:{int(min_out_h)}:{sec_out_min}")

print()
print('-------')
print()

hh = time_in_sec // 3600
mm = ((time_in_sec / 3600) - hh)  * 60
ss = (mm - int(mm)) * 60

print(f"{(hh)}:{int(mm)}:{round(ss)}")

