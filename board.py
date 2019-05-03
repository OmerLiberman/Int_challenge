X_COORD = 0
Y_COORD = 1


class Board:
    """
    This class describes the game board.
    """

    FREE_SEAT_SIGN = '-'
    BOX_SIGN = 'B'
    HUNTER_SIGN = 'H'

    def __init__(self, n, b, h, n_is_even):
        """
        Init method
        :param n: board size.
        :param b: num of boxes placed on board.
        :param h: num of hunters placed on board.
        :param n_is_even: if the board size is even.
        """
        self.N = n
        self.B = b
        self.H = h
        self.is_N_even = n_is_even
        self.boxes_by_parts, self.hunters_by_part = [], []

    def split_boxes_hunters_when_size_is_even(self, array_of_boxes_placed_coords, array_of_hunters_placed_coords):
        """
        A B
        D C
        :param array_of_boxes_placed_coords:
        :param array_of_hunters_placed_coords:
        :return:
        """
        boxes_a, hunters_a = [], []
        boxes_b, hunters_b = [], []
        boxes_c, hunters_c = [], []
        boxes_d, hunters_d = [], []

        for box in array_of_boxes_placed_coords:
            if self._is_coord_in_left_halve(box[X_COORD], box[Y_COORD]):
                if self._is_coord_in_up_halve(box[X_COORD], box[Y_COORD]):
                    boxes_a.append(box)
                else:  # left - down (D)
                    boxes_d.append(box)
            else:  # right halve
                if self._is_coord_in_up_halve(box[X_COORD], box[Y_COORD]):
                    boxes_b.append(box)
                else:  # right - down (C)
                    boxes_c.append(box)

        for hunter in array_of_hunters_placed_coords:
            if self._is_coord_in_left_halve(hunter[X_COORD], hunter[Y_COORD]):
                if self._is_coord_in_up_halve(hunter[X_COORD], hunter[Y_COORD]):
                    hunters_a.append(hunter)
                else:  # left - down (D)
                    hunters_d.append(hunter)
            else:  # right halve
                if self._is_coord_in_up_halve(hunter[X_COORD], hunter[Y_COORD]):
                    hunters_b.append(hunter)
                else:  # right - down (C)
                    hunters_c.append(hunter)

        self.boxes_by_parts = [boxes_a, boxes_b, boxes_c, boxes_d]
        self.hunters_by_part = [hunters_a, hunters_b, hunters_c, hunters_d]

    def _is_coord_in_left_halve(self, x, y):
        return x - 1 < self.N / 2

    def _is_coord_in_up_halve(self, x, y):
        return y - 1 > self.N / 2
