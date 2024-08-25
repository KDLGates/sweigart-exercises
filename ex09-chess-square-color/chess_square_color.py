# This program implements a function to return chessboard square properties such as white/black.

# Create the 2D array representation
chessboard = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]

# Create a dictionary of square properties
square_properties = {}

for row in range(8):
    for col in range(8):
        square = chessboard[row][col]
        is_light = (row + col) % 2 == 0
        square_properties[square] = {
            'color': 'white' if is_light else 'black',
            'row': 8 - row,
            'col': col + 1
        }

## Example usage:
# print(chessboard[0][0])  # Output: 'a8'
# print(square_properties['e4'])  # Output: {'color': 'light', 'row': 4, 'col': 5}

def get_chess_square_color(col, row):
    try:
        return square_properties[chessboard[col][row]]['color']
    except(IndexError):
        return ''

assert get_chess_square_color(0, 0) == 'white'
assert get_chess_square_color(1, 0) == 'black'
assert get_chess_square_color(0, 1) == 'black'
assert get_chess_square_color(7, 7) == 'white'
assert get_chess_square_color(0, 8) == ''
assert get_chess_square_color(2, 9) == ''
assert get_chess_square_color(0, 7) == square_properties['h8']['color']
