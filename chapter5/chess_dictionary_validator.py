ALLOWED_PIECE_COUNT = {
    "king": 1,
    "queen": 1,
    "rook": 2,
    "bishop": 2,
    "knight": 2,
    "pawn": 8,
}
BLACK_PIECE_CH = "b"
WHITE_PIECE_CH = "w"
ALLOWED_BOARD_ROWS = ["1", "2", "3", "4", "5", "6", "7", "8"]
ALLOWED_BOARD_COLS = ["a", "b", "c", "d", "e", "f", "g", "h"]


def is_valid_chess_board(board: dict) -> bool:
    b_count_dict: dict[str, int] = {}
    w_count_dict: dict[str, int] = {}
    for v in board.values():
        # check that they begin with b/w
        if v[0] != BLACK_PIECE_CH and v[0] != WHITE_PIECE_CH:
            return False
        # check that after the first char follows a valid name
        if v[1:] not in ALLOWED_PIECE_COUNT:
            return False
        else:
            # count each kind of piece
            if v[0] == BLACK_PIECE_CH:
                b_count_dict.setdefault(v[1:], 0)
                b_count_dict[v[1:]] += 1
            elif v[0] == WHITE_PIECE_CH:
                w_count_dict.setdefault(v[1:], 0)
                w_count_dict[v[1:]] += 1
    # check that each colour has the appropiate number of pieces
    if sum(b_count_dict.values()) > 16 or sum(w_count_dict.values()) > 16:
        return False
    for k in b_count_dict.keys():
        if b_count_dict[k] > ALLOWED_PIECE_COUNT[k]:
            return False
    for k in w_count_dict.keys():
        if w_count_dict[k] > ALLOWED_PIECE_COUNT[k]:
            return False
    # check if the pieces are on valid spaces
    for k in board:
        if k[0] not in ALLOWED_BOARD_ROWS or k[1] not in ALLOWED_BOARD_COLS:
            return False
    return True


def main():
    board = {
        "1h": "bking",
        "6c": "wqueen",
        "2g": "bbishop",
        "5h": "bqueen",
        "3e": "wking",
    }
    print(is_valid_chess_board(board))


if __name__ == "__main__":
    main()
