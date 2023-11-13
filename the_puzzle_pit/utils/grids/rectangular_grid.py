class RectangularGrid(list):
    def __init__(self,
                 width: int,
                 height: int,
                 dvalue=None,
                 dfactory=None,
                 ):
        """

        :param width:
        :param height:
        :param dvalue: Specifies a fixed default value for all cells.
        :param dfactory: Specifies a factory function(e.g. a constructor) that creates cells dynamically based on their
        grid coordinates. D
        """
        super().__init__([[dfactory(x, y) if dfactory else dvalue for y in range(width)] for x in range(height)])

    @property
    def columns(self):
        return [[row[j] for row in self] for j in range(self.width)]

    @property
    def height(self):
        return len(self)

    @property
    def rows(self):
        return self

    @property
    def width(self):
        return len(self[0]) if self else 0


