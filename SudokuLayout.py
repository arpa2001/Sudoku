import random

def rndmint(n1, n2):    # Shortcut to random.randint()
    return random.randint(n1, n2)

def randmchoice(n1, n2, inplist):   # Prevents Repeats
    buff_list = []
    for i in range(n1,int(n2)+1):
        buff_list.append(i)
    if not inplist == []:
        for j in inplist:
            buff_list.remove(j)
    buff_value = random.choice(buff_list)
    inplist.append(buff_value)


board_size = input("Enter Board size:\n\t1 for easy\n\t2 for medium\n\t3 for hard\n: ")
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
print('\n')

# Selecting which sections to preload with numbers
secs2fill = []
for i in range(rndmint(1,sections)):
    randmchoice(1,sections,secs2fill)
secs2fill.sort()

# Selecting selected sections' locations to fill with values
board = {}
for i in secs2fill:
    sec_locs = []
    for j in range(rndmint(1,8)):
        randmchoice(1, 9, sec_locs)
    board[i] = sec_locs

# Making the Board
game_board = {}
for i in range(sections):
    for j in range(9):
        place = str(i+1) + '.' + str(j+1)
        game_board[place] = ' '

# Selecting values on the board
for i in board:
    board.get(i).sort()
    for j in board.get(i):
        cell_fill = str(i) + '.' + str(j)
        check = []

        # Checking the section
        for k in range(1,10):
            place = str(i) + '.' + str(k)
            if not cell_fill == place:
                if not game_board[place] == ' ':
                    check.append(game_board.get(place))
        
        # Checking the column
        l = i
        m = j
        while(l > int((length/3))):
            l -= int((length/3))
        while(m > 3):
            m -= 3
        l_fixed = l
        m_fixed = m
        while(l <= ((((length/3)-1)*3)+l_fixed)):
            m = m_fixed
            while(m <= (m_fixed + 6)):
                place = str(l) + '.' + str(m)
                if not cell_fill == place:
                    if not game_board[place] == ' ':
                        check.append(game_board.get(place))
                m += 3
            l += int((length/3))
        
        # Checking the row
        n = i
        o = j
        first_rowvalue = []
        f_value = 1
        for x in range(int(length/3)):
            first_rowvalue.append(f_value)
            f_value += int(length/3)
        while(not (n in first_rowvalue)):
            n -= 1
        while(not (o == 1 or o == 4 or o == 7)):
            o -= 1
        n_fixed = n
        o_fixed = o
        while(n <= (((length/3)-1)+n_fixed)):
            o = o_fixed
            while(o <= (o_fixed + 2)):
                place = str(n) + '.' + str(o)
                if not cell_fill == place:
                    if not game_board[place] == ' ':
                        check.append(game_board.get(place))
                o += 1
            n += 1
        
        # Finalising Value
        numbers = [1,2,3,4,5,6,7,8,9]
        check = list(set(check))
        if not check == []:
            for p in check:
                numbers.remove(p)
        number = random.choice(numbers)
        game_board[cell_fill] = int(number)


# Priting Layout

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
            place = str(place_value) + '.' + str(block_value)
            print(f"{game_board.get(place)} ", end='')
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

print('\n')
