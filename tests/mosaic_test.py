from the_puzzle_pit.mosaic.mosaic import Mosaic

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


class TestMosaicFunctionality:
    pass
