board_size = input(
    "Enter Board size:\n\t1 for easy\n\t2 for medium\n\t3 for hard\n: ")
# Selecting the number of sections
rep = True
while(rep):
    if board_size == '1':
        sections = 1
        length = 3
        rep = False
    elif board_size == '2':
        sections = 4
        length = 6
        rep = False
    elif board_size == '3':
        sections = 9
        length = 9
        rep = False
    else:
        board_size = input("Wrong selection.\n\tChoose Again: ")

i = 0
counter = 1
lift = 0
print('-'*(8*(int(length/3)) + 1))
while(i < (length)):
    j = 0
    print('| ', end='')
    while(j < (length/3)):
        for k in range(3):
            block_value = k + 1 + (i % 3)*3
            place_value = j + 1 + lift
            print(f"{place_value}.{block_value} ", end='')
        print('| ', end='')
        j += 1
    print('\n', end='')
    if block_value == 9:
        print('-'*(8*(int(length/3)) + 1))
    i += 1
    if counter == 3:
        counter = 1
        lift += int(length/3)
    else:
        counter += 1