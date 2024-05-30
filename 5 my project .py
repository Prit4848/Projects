def sum(a, b, c):
    return a + b + c

def printbord(xstate, zstate):
    zero = 'x' if xstate[0] else ('0' if zstate[0] else ' ')
    one = 'x' if xstate[1] else ('0' if zstate[1] else ' ')
    two = 'x' if xstate[2] else ('0' if zstate[2] else ' ')
    three = 'x' if xstate[3] else ('0' if zstate[3] else ' ')
    four = 'x' if xstate[4] else ('0' if zstate[4] else ' ')
    five = 'x' if xstate[5] else ('0' if zstate[5] else ' ')
    six = 'x' if xstate[6] else ('0' if zstate[6] else ' ')
    seven = 'x' if xstate[7] else ('0' if zstate[7] else ' ')
    eight = 'x' if xstate[8] else ('0' if zstate[8] else ' ')
    
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("x won the match")
            return 1
        elif sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("0 won the match")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x and 0 for o
    print("Welcome to Tic Tac Toe")
    while True:
        printbord(xstate, zstate)
        if turn == 1:
            print("x's chance")
            value = int(input("Please enter a value: "))
            xstate[value] = 1
        else:
            print("0's chance")
            value = int(input("Please enter a value: "))
            zstate[value] = 1
        cwin = checkwin(xstate, zstate)
        if cwin != -1:
            break
        turn = 1 - turn
