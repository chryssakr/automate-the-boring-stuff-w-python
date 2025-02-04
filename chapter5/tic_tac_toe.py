def print_board(board):
    print(f"\n{board["top-L"]}|{board["top-M"]}|{board["top-R"]}")
    print("-+-+-")
    print(f"{board["mid-L"]}|{board["mid-M"]}|{board["mid-R"]}")
    print("-+-+-")
    print(f"{board["low-L"]}|{board["low-M"]}|{board["low-R"]}\n")


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
    for _ in range(9):
        print("\nValid possible moves:")
        for k, v in the_board.items():
            if v == " ":
                print(k, end=" ")
        move = input(f"\nTurn for {turn}. Move on which space?\n")
        the_board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        print_board(the_board)


if __name__ == "__main__":
    main()
