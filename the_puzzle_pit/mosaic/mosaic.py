class _Tile:
    def __init__(self, clue):
        if clue == -1:
            self._clue = None
        else:
            self._clue = clue
            self.connections_out = []
        self.connections_in = []

    @property
    def clue(self):
        return self._clue

class Mosaic(list):
    def __init__(self, clues: list[list[int, ...], ...]):
        super().__init__()
        self._clues = clues
        self._clue_tiles = []
        self._height = len(clues)
        self._width = len(clues[0])
        for clue_row in clues:
            row = []
            for clue in clue_row:
                if clue == -2:
                    row.append(None)
                elif -1 <= clue <= 9:
                    tile = _Tile(clue)
                    row.append(tile)
                    if clue >= 0:
                        self._clue_tiles.append(tile)
            self.append(row)

        # create connections
        for (i, row) in enumerate(self):
            for (j, tile) in enumerate(row):
                if tile.clue is not None:
                    for (di, dj) in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)):
                        other_i = i + di
                        other_j = j + dj
                        if 0 <= other_i < self._height and 0 <= other_j < self._width:
                            other_tile = self[other_i][other_j]
                            tile.connections_out.append(other_tile)
                            other_tile.connections_in.append(tile)


    @property
    def clues(self):
        return [[tile.clue if tile is not None else None for tile in row] for row in self]

    @property
    def clue_tiles(self):
        return self._clue_tiles

    def flatten(self):
        return [tile for row in self for tile in row]
