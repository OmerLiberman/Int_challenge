from board import Board


class Case:

    def __init__(self, n, b, h, boxes_coords, hunters_coords):
        is_size_even = (n % 2 == 0)
        self.board = Board(n, b, h, is_size_even)
        self.board.place_boxes_and_hunters(boxes_coords, hunters_coords)

    def solve(self):
        return 0
