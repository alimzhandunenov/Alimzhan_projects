arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(arr)):
    arr[i].islower()
last_len = len(arr)

for i in range(len(arr)):
    temporary_list = arr[i].split(" ")
    hm_indexes = len(temporary_list) -1
    temporary_name = temporary_list[hm_indexes]
    name = temporary_name.lower().title()
    arr.append(name)

print(arr)
for words in arr:
    print(words)
    arr.remove(words)