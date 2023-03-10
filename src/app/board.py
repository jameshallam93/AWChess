import itertools
from pieces import *
from adapters.ui import ui_console


def get_empty_board():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    return {
        "".join(pair): {
            "piece": None,
            "coords": (letters.index(pair[0]), numbers.index(pair[1]))
        } for pair in itertools.product(letters, numbers)}


PIECE_MAP = {
    "K": {
        "name": "King",
        "start": ["E1", "E8"],
        "piece": King
    },
    "Q": {
        "name": "Queen",
        "start": ["D1", "D8"],
        "piece": Queen
    },
    "R": {
        "name": "Rook",
        "start": ["A1", "H1", "A8", "H8"],
        "piece": Rook
    },
    "B": {
        "name": "Bishop",
        "start": ["C1", "F1", "C8", "F8"],
        "piece": Bishop
    },
    "N": {
        "name": "Knight",
        "start": ["B1", "G1", "B8", "G8"],
        "piece": Knight
    },
    "P": {
        "name": "Pawn",
        "start": ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
                  "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
        "piece": Pawn
    }
}

PIECE_MAP_SINGLE_PAWNS = {
    "P": {
        "name": "Pawn",
        "start": ["D2", "D7"],
        "piece": Pawn
    }
}


def board_factory(piece_map=PIECE_MAP):
    board = get_empty_board()
    for _p, data in piece_map.items():
        for coord in data["start"]:
            board[coord]["piece"] = data["piece"](coord)
    return board


ui = ui_console.ui()

ui['render'](board_factory())


