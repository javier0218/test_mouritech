
def uncommon_words():
    value_1 = input('Enter a string: ')
    value_2 = input('Enter a string2: ')
    list_1 = value_1.split()
    list_2 = value_2.split()
    temp = ''

    for i in list_1:
        if i not in list_1:
            temp = temp + " "+i

    for j in list_2:
        if j not in list_1:
            temp = temp + " " + j

    print(temp)

uncommon_words()

























