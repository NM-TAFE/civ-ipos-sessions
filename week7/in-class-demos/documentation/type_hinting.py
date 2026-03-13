# Original inspiriation courtesy of @ZuidVol
from typing import Callable, Literal, Optional, TypeAlias, Tuple

# --- Domain types ---
Player: TypeAlias = Literal["X", "O"]
BoardCell: TypeAlias = Optional[Player]       
Board: TypeAlias = list[list[BoardCell]]  


class TicTacToe:
    def __init__(self, board_state: Board) -> None:
        pass

    def get_next_player(self) -> Player:
        """
        Return the next player to move.
        (Placeholder implementation to make the example type-complete.)
        """
        pass

    @staticmethod
    def get_board_position_from_index(idx: int) -> Tuple[int, int]:
        """
        Map a linear index [0..8] to a (row, col) position on a 3x3 board.
        """
        pass

    def get_next_move(self, user_input: Callable[[Player], int]) -> Board:
        """
        Ask for the next move from a callback that accepts the current Player and
        returns a board index (0..8). If the target cell is empty, apply the move
        and return the updated board.
        """
        pass