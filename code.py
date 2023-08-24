def draw_board(b):
    print(f"{b[0]} | {b[1]} | {b[2]} ")
    print("_________")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("_________")
    print(f"{b[6]} | {b[7]} | {b[8]}")


def check(b):
    for i in range(0, 9, 3):
        if b[i] == b[i + 1] == b[i + 2] and b[i] != ' ':
            return b[i]
    for i in range(0, 3):
        if b[i] == b[i + 3] == b[i + 6] and b[i] != ' ':
            return b[i]
    if b[0] == b[4] == b[8] and b[0] != ' ':
        return b[0]
    elif b[2] == b[4] == b[6] and b[2] != ' ':
        return b[2]
    l = 0
    for i in range(0, 9):
        if b[i] != ' ':
            l += 1
    if l == 9:
        return "Draw"
    return 0


if __name__ == '__main__':
    print("Rules:")
    i = 1
    b = [' '] * 9
    print(f'{i}.Enter player 1 choice at first')
    i += 1
    print(f'{i}.Player 1 can only choose X or O')
    i += 1
    print(f'{i}.After choosing the symbol ,Each player should enter there coordinates alternatively')
    i += 1
    print(f'{i}.Coordinates range between 1-9')
    print("*** Enjoy the game ****\n\n\n")
    print("*********** TIC TAC TOE ***********")
    l = []
    while (1):
        choice = input("Player 1 choice (choose X or O):")
        ch = ""
        if choice == 'x' or choice == "X":
            choice = 'X'
            ch = 'O'
            break
        elif choice == 'o' or choice == "O":
            choice = 'O'
            ch = 'X'
            break
        else:
            print("Invalid Input")
    print(f"Player 1 :{choice}   Player 2 :{ch}")
    draw_board(b)
    c = 1
    while (1):
        x = int(input(f'Player {c} coordinates:'))

        if x < 1 or x > 9:
            print("Invalid")
        elif x not in l:
            if c == 1:
                b[x - 1] = choice
            else:
                b[x - 1] = ch
            draw_board(b)
            if c == 1:
                c = 2
            else:
                c = 1
            l.append(x)
        else:
            print('Invalid Input')
        win = check(b)
        if win == choice:
            print("Player 1 WINS")
            break
        elif win == ch:
            print("Player 2 WINS")
            break
        elif win == "Draw":
            print("Draw")
            break
