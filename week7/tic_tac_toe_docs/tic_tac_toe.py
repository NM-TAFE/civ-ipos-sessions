board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    '''Prints the Tic-Tac-Toe board'''
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_win(player, board):
    '''Check rows, columns, and diagonals for win condition for a given player
    
    Parameters:
    - player: str - The player ('X' or 'O') to check for win
    - board: list[list[str]] - The game board
    
    Returns:
    - bool: True if the player wins, False otherwise
    '''
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tally_wins(results):
    '''Tally the number of wins from a list of results
    
    Parameters:
    - results: list - List of boolean results indicating win (True) or loss (False)
    
    Returns:
    - int: Total number of wins
    '''
    return sum(results)

def main():
    '''Main function to control the Tic-Tac-Toe game'''
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(current_player)
                results.append(win)
                if win:
                    print_board()
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print("Invalid input! Please enter row and column values within the range (0-2).")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")

if __name__ == "__main__":
    main()
