class _Tile:
    def __init__(self, clue):
        if clue == -1:
            self._clue = None
        else:
            self._clue = clue
            self.connections_out = []
        self._colour = -1
        self.connections_in = []

    @property
    def clue(self):
        return self._clue

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour
        for clue_tile in self.connections_in:
            clue_tile.check()

    def check(self):
        # Divide outgoing connections into those that have already been coloured and those that are still open.
        connections_out_coloured = []
        connections_out_uncoloured = []
        for tile in self.connections_out:
            if tile.colour == -1:
                connections_out_uncoloured.append(tile)
            else:
                connections_out_coloured.append(tile)
        sum_of_coloured_connections = sum([tile.colour for tile in connections_out_coloured])
        # Heuristic 1: If the sum of already coloured connections matches the clue, colour all remaining connections white (0)
        if sum_of_coloured_connections == self._clue:
            for tile in connections_out_uncoloured:
                tile.colour = 0
        # Heuristic 2: If the number of uncoloured connections matches the number of those that are yet to be coloured black,
        # colour all remaining connections black (1)
        elif len(connections_out_uncoloured) == self._clue - sum_of_coloured_connections:
            for tile in connections_out_uncoloured:
                tile.colour = 1


class Mosaic(list):
    def __init__(self, clues: list[list[int, ...], ...]):
        super().__init__()
        self._clues = clues
        self._clue_tiles = []
        self._height = len(clues)
        self._solved = False
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

    def solve(self):
        if not self._solved:
            for clue_tile in self._clue_tiles:
                clue_tile.check()
        self._solved = True
        return [[tile.colour if tile is not None else -2 for tile in row] for row in self]
