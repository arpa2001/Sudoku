from random import randint,choice


board_size = int(input("Enter Board size:\n\t1 for easy\n\t2 for medium\n\t3 for hard\n: "))

# Selecting the number of sections
rep = True
while board_size not in [1,2,3]:
    board_size = int(input("Wrong selection.\n\tChoose Again: "))
print('\n')

sections = board_size**2
length = board_size*3

# Selecting which sections to preload with numbers
secs2fill = list(range(1,sections))
for _ in range(randint(0, sections-1)):
    secs2fill.remove(choice(secs2fill))

# Selecting selected sections' locations to fill with values
board = {}
nums = list(range(1,10))
for i in secs2fill:
    board[i] = nums.copy()
    for _ in range(randint(1,8)):
        board[i].remove(choice(board[i]))

# Making the Board
game_board = {}
for i in range(sections):
    for j in range(9):
        game_board[(i+1, j+1)] = ' '

# Selecting values on the board
for i in board:
    for j in board[i]:
        cell_fill = (i,j)
        check = []

        # Checking the section
        for k in range(1,10):
            if cell_fill != (i,k):
                if game_board[(i, k)] != ' ':
                    check.append(game_board[(i, k)])
        
        # Checking the column
        l = i
        m = j
        while l>(length/3):
            l -= (length/3)
        while(m > 3):
            m -= 3
        l_fixed = l
        m_fixed = m
        while(l <= ((((length/3)-1)*3)+l_fixed)):
            m = m_fixed
            while(m <= (m_fixed + 6)):
                if cell_fill != (l,m):
                    if game_board[(l,m)] != ' ':
                        check.append(game_board[(l,m)])
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
                if cell_fill != (n,o):
                    if game_board[(n,o)] != ' ':
                        check.append(game_board[(n,o)])
                o += 1
            n += 1
        
        # Finalising Value
        numbers = [1,2,3,4,5,6,7,8,9]
        check = list(set(check))
        if check:
            for p in check:
                numbers.remove(p)
        number = choice(numbers)
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
            print(f"{game_board[(place_value,block_value)]} ", end='')
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
