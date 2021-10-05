for i in range(100):
    new_str = str(i+1)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and i+1 != 11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1]) > 1 and int(new_list[-1]) <= 4:
        if  i+1 > 10 and i+1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))
