'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
# Game state
p1 = "X"
p2 = "O"
empty = " "
board = [empty] * 9

# Game loop
while True:
    # Print board
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

    # Check for win
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player", board[wc[0]], "wins!")
            exit(0)

    # Check for tie
    if empty not in board:
        print("It's a tie!")
        exit(0)

    # Get next move
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            board[int(move)] = player
            break
        else:
            print("Invalid move, try again.")
