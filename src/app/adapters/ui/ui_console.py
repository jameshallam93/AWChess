
class Bcolors():
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'


def print_board(board):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for number in numbers:
        for letter in letters:
            piece = board[letter + number]["piece"]
            if piece:
                if piece.color == "white":
                    print(Bcolors.OKCYAN + piece.icon, end=" ")
                else:
                    print(Bcolors.OKGREEN + piece.icon, end=" ")
            else:
                print(" ", end=" ")
        print("")

def ui():
    render = print_board
    return {
        "render": render
    }

