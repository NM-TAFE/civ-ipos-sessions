empty = " "
board = [empty] * 9

class P1():
    def __init__(self, move):
        self.move = move

    def next_move(self):
        while True:
            player = "1"
            self.move = input("Next move for player " + player + " (0-8): ")
            if self.move.isdigit() and 0 <= int(self.move) <= 8 and board[int(self.move)] == empty:
                board[int(self.move)] = player
                break
            else:
               print("Invalid move, try again.")
class P2():
    def __init__(self, move):
        self.move = move

    def next_move(self):
        while True:
            player = "2"
            self.move = input("Next move for player " + player + " (0-8): ")
            if self.move.isdigit() and 0 <= int(self.move) <= 8 and board[int(self.move)] == empty:
                board[int(self.move)] = player
                break
            else:
               print("Invalid move, try again.")

class Check:
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player", board[wc[0]], "wins!")
            exit(0)

        # Check for tie
        if empty not in board:
            print("It's a tie!")
            exit(0)

class Board:
    empty = " "
    board = [empty] * 9

    while True:
    # Print board
        print(board[0], "|", board[1], "|", board[2])
        print("---------")
        print(board[3], "|", board[4], "|", board[5])
        print("---------")
        print(board[6], "|", board[7], "|", board[8])
        print()
        break

board = Board()
p1 = P1()
check = Check()
p2 = P2()
check = Check()


