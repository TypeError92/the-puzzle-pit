from the_puzzle_pit.utils.grids import RectangularGrid


class TestRectangularGrid:
    def test_rectangular_grid_00(self):
        """Creates an empty rectangular grid with the specified dimensions."""
        grid = RectangularGrid(3, 2)
        assert (grid.width, grid.height) == (3, 2)
        assert grid == grid.rows == [[None, None, None], [None, None, None]]
        assert grid.columns == [[None, None], [None, None], [None, None]]

    def test_rectangular_grid_01(self):
        """Allows for the specification of a fixed default value."""
        grid = RectangularGrid(2, 1, dvalue=4)
        assert grid == [[4, 4]]

    def test_rectangular_grid_02(self):
        """Allows for the specification of a generator that takes the cell's row and column as arguments.."""
        grid = RectangularGrid(2, 3, dfactory=lambda x, y: (x, y))
        assert grid == [[(0, 0), (0, 1)], [(1, 0), (1, 1)], [(2, 0), (2, 1)]]
