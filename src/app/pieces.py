

class Piece():
    def __init__(self, config):
        self.coords = config["start"]
        self.name = config["name"]
        self.icon = config["icon"]
        self._color = self._init_color(config["start"])

    def _init_color(self, coords):
        y = coords[1]
        if y in ["1", "2", "3", "4"]:
            return "white"
        return "black"

    @property
    def color(self):
        return self._color


class Pawn(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "Pawn",
            "icon": "♙",
            "start": coords
        })


class Bishop(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "Bishop",
            "icon": "♗",
            "start": coords
        })


class Rook(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "Rook",
            "icon": "♖",
            "start": coords
        })


class Knight(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "Knight",
            "icon": "♘",
            "start": coords
        })


class Queen(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "Queen",
            "icon": "♕",
            "start": coords

        })


class King(Piece):
    def __init__(self, coords):
        super().__init__({
            "name": "King",
            "icon": "♔",
            "start": coords
        })
