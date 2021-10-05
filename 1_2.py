list_of_cubs = []
add_list_of_cubs = []
all_sum = 0

    # Каждый элемент возводим в куб при добавлении в список

for i in range(1, 1000, 2):
    list_of_cubs.append(i**3)

    # Перебираем элементы списка

    for ind, val in enumerate(list_of_cubs):
        sum_digits = 0
        while val > 0:
            sum_digits += val % 10
            val //= 10
            if sum_digits % 7 == 0:
                all_sum += list_of_cubs[ind]

print(all_sum)

for m in list_of_cubs:
    add_list_of_cubs.append(m + 17)

all_sum = 0

for ind, val in enumerate(add_list_of_cubs):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += add_list_of_cubs[ind]

print(all_sum)



