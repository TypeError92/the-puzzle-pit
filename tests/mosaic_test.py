from the_puzzle_pit.mosaic.mosaic import Mosaic, _Tile

easy_5x5 = (
    [
        [-1, 2, -1, -1, 1],
        [-1, -1, 2, -1, -1],
        [6, -1, 3, -1, 3],
        [-1, -1, 3, -1, 4],
        [-1, 3, -1, -1, -1]
    ],
    [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1]
    ]
)


class TestMosaicInit:
    def test_mosaic_init_00(self):
        """Should accept an n x n matrix of integers [-1, 9] as its only argument."""
        try:
            Mosaic(easy_5x5[0])
        except:
            assert False

    def test_mosaic_init_01(self):
        """Should create:
        - a .grid property with a matrix matching the shape of the input and containing:
            - a cell with a clue for each input value >= 0
            - a cell with clue is None for each input value == -1
        - a .clue_cells property listing only those cells containing a clue"""
        clues = easy_5x5[0]
        mosaic = Mosaic(clues)
        assert len(mosaic) == 5
        assert all([len(row) == 5 for row in mosaic])
        assert len(mosaic.clue_tiles) == 9

    def test_mosaic_init_02(self):
        """Allows for retrieval of original input via .clues property."""
        clues = easy_5x5[0]
        mosaic = Mosaic(clues)
        assert mosaic.clues == clues

    def test_mosaic_init_03(self):
        """Accepts input values of -2 as 'fillers' for non-rectangular shapes and marks these as None in the .grid."""
        clues = [
            [-1, 2, -1, -1, -2],
            [-1, -1, 2, -1, -1],
            [6, -1, 3, -1, 3],
            [-1, -1, 3, -1, 4],
            [-1, 3, -1, -1, -1]
        ]
        mosaic = Mosaic(clues)
        assert mosaic[0][4] is None

    def test_mosaic_init_04(self):
        """Creates an "in" connection between each tile and all of its neighbouring clue_tiles (including itself where appropriate)."""
        clues = easy_5x5[0]
        mosaic = Mosaic(clues)
        assert [[len(tile.connections_in) for tile in row] for row in mosaic] == [
            [1, 2, 2, 2, 1],
            [2, 4, 3, 4, 2],
            [1, 4, 3, 5, 2],
            [2, 4, 3, 4, 2],
            [1, 2, 2, 2, 1]
        ]

    def test_mosaic_init_05(self):
        """Creates an "out" connection between each clu_tile and all of its neighbouring tiles (including itself)."""
        clues = easy_5x5[0]
        mosaic = Mosaic(clues)
        assert [len(clue_tile.connections_out) for clue_tile in mosaic.clue_tiles] == [6, 4, 9, 6, 9, 6, 9, 6, 6]


class TestMosaicUtils:
    def test_mosaic_flatten(self):
        """Mosaic.flat() returns a flattened list containing all the mosaic's tiles."""
        clues = easy_5x5[0]
        mosaic = Mosaic(clues)
        flattened = mosaic.flatten()
        assert len(flattened) == 25
        assert all([isinstance(tile, _Tile) for tile in flattened])


class TestMosaicInputValidation:
    pass


class TestMosaicSolve:
    """Should return the correct solution for an easy 5 x 5 puzzle."""
    def test_mosaic_solve_00(self):
        clues, solution = easy_5x5
        mosaic = Mosaic(clues)
        assert mosaic.solve() == solution



class TestTile:
    pass
