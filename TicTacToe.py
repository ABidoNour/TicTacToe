class Board:
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(0)

    def __str__(self):
        board = ""
        for i in range(3):
            row = ""
            for j in range(3):
                if self.board[i][j] == 0:
                    row += "   "
                else:
                    row += f" {self.board[i][j]} "
                row += "┃" if j != 2 else ""
            board += row + "\n"
            if i != 2:
                board += "━━━╋━━━╋━━━\n"
        return board


def game(board, turn_num=0, play1=True):
    print("Shehab will lose")
    while True:
        print(f"Turn {turn_num}:")
        print(board)
        if play1:
            turn(board.board, "1")
            play1 = False
        else:
            turn(board.board, "2")
            play1 = True
        if is_win(board.board) == "X":
            print("Player 1 wins")
            print(board)
            break
        if is_win(board.board) == "O":
            print("Player 2 wins")
            print(board)
            break
        if is_full(board.board):
            print("Draw")
            print(board)
            break
        turn_num += 1


def is_win(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]


def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def turn(board, player):
    ltr = "X" if player == "1" else "O"
    coord = input(
        f"Player {player} type in the row number then column number to place a {ltr}:\nEx: '2,0' for bottom left.\n")
    while True:
        if len(coord) != 3 or (int(coord[0]) not in range(0, 3)) or (
                int(coord[2]) not in range(0, 3)) or coord[1] != ",":
            coord = input(
                "Type again with correct format (Row number from 0 to 2,column number from 0 to 2)\n")
            continue
        if board[int(coord[0])][int(coord[2])] != 0:
            coord = input("Space already filled\n")
            continue
        break
    board[int(coord[0])][int(coord[2])] = ltr


def main():
    board = Board()
    game(board)


if __name__ == '__main__':
    main()
