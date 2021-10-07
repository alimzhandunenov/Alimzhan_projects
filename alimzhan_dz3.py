list_one = list(range(21, 92, 10)) + [1]
list_two = list(range(2, 5))
list_three = list(range(11, 15))
n = 1
end = n % 10
while n <= 100:
    if n in list_three:
        print(n, 'процентов')
        n += 1
        end = n % 10
    elif end in list_two:
        print(n, 'процента')
        n += 1
        end = n % 10
    elif end in list_one:
        print(n, 'процент')
        n += 1
        end = n % 10
    else:
        print(n, 'процентов')
        n += 1
        end = n % 10




