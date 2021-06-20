board= [" "  for i in range(9)]

def print_board():
    row1= f"|{board[0]}|"f" " f"|{board[1]}|"f" " f"|{board[2]}|"
    row2= f"|{board[3]}|"f" " f"|{board[4]}|"f" " f"|{board[5]}|"
    row3= f"|{board[6]}|"f" " f"|{board[7]}|"f" " f"|{board[8]}|"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):

    if icon== "X":
        number= 1
    elif icon == "O":
        number= 2
    print(f"Your turn player {number}")
    choice= int(input("Enter the no from 1 to 9:\n"))
    if board[choice-1]== " ":
        board[choice-1]= icon

    else:
        print("The space is taken")

def is_victory(icon):
    if (board[0]== icon and board[1]== icon and board[2]== icon) or (board[3]== icon and board[4]== icon and board[5]== icon) or (board[6]== icon and board[7]== icon and board[8]== icon) or (board[0]== icon and board[3]== icon and board[6]== icon) or (board[1]== icon and board[4]== icon and board[7]== icon) or (board[2]== icon and board[5]== icon and board[8]== icon) or (board[0]== icon and board[4]== icon and board[8]== icon) or (board[2]== icon and board[4]== icon and board[6]== icon):

        return True

    else:
        return False
    
while True:
    print_board()
    player_move("X")
    print_board()
    if (is_victory("X")):
        print("X is the winner")
        break

    player_move("O")
    if is_victory("O"):
        print_board()
        print("Y is the winner")
        break
        