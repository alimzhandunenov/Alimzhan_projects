
my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)
# a
final_sum = 0  # финальный ответ'

for num in my_list:
    check_sum = 0  # сумма всех цифр конкретного числа
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

# b&c
final_sum = 0
for num in my_list:
    num += 17  # отличие от a
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)