def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


def main():
    the_board = {
        "top-L": " ",
        "top-M": " ",
        "top-R": " ",
        "mid-L": " ",
        "mid-M": " ",
        "mid-R": " ",
        "low-L": " ",
        "low-M": " ",
        "low-R": " ",
    }
    print_board(the_board)
    turn = "X"
    for i in range(9):
        move = input(f"Turn for {turn}. Move on which space?")
        the_board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        print_board(the_board)


if __name__ == "__main__":
    main()
