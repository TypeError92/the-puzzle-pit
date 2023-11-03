## Properties
### box_height
type: `int`  
The height of a box within the sudoku. Must be a factor of `height`. Defaults to the square root of `height`.
### box_width
type: `int`  
The width of a box within the sudoku. Must be a factor of `width`. 
### height
type: `int`  
The total height of the sudoku. Defaults to `9`.
### size
type: `int`
Defines the height/width of the sudoku, i.e. the number of cells per column/row/box.
### diagonal
type: `bool`
If set to `True`, adds an additional rule to the sudoku according to which each diagonal (top-left to bottom-right,
top-right to bottom-left) must also contain each number from 1 to `size` exactly once.