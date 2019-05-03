X_COORD = 0
Y_COORD = 1


class Board:
    """
    This class describes the game board.
    """

    FREE_SEAT_SIGN = '-'
    BOX_SIGN = 'B'
    HUNTER_SIGN = 'H'

    def __init__(self, n, b, h, n_is_even=True):
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
        self.board = [[self.FREE_SEAT_SIGN for x in range(self.N)] for y in range(self.N)]
        self.is_N_even = n_is_even

        self.hunters_left_halve, self.hunters_right_halve = 0, 0
        self.boxes_left_halve, self.boxes_right_halve = 0, 0
        self.free_seats_left_halve, self.free_seats_right_halve = 0, 0

        self.hunters_up_halve, self.hunters_down_halve = 0, 0
        self.boxes_up_halve, self.boxes_down_halve = 0, 0
        self.free_seats_up_halve, self.free_seats_down_halve = 0, 0

    def place_boxes_and_hunters(self, array_of_boxes_placed_coords, array_of_hunters_placed_coords):
        """
        :param array_of_boxes_placed_coords:
                array of tuples of coordinates (x,y) which indicate where the boxes are
                placed on the board.
        :param array_of_hunters_placed_coords:
                array of tuples of coordinates (x,y) which indicate where the hunters are
                placed on the board.
        :return: nothing.
        """
        for box in array_of_boxes_placed_coords:
            self.board[box[X_COORD] - 1][box[Y_COORD] - 1] = self.BOX_SIGN
            self.hunters_boxes_free_seats_counter_by_side(box)

        for hunter in array_of_hunters_placed_coords:
            self.board[hunter[X_COORD] - 1][hunter[Y_COORD] - 1] = self.HUNTER_SIGN
            self.hunters_boxes_free_seats_counter_by_side(hunter)

        self.update_free_seats_by_side_counter()

    def hunters_boxes_free_seats_counter_by_side(self, coords):
        """
        Complicated name for simple method.
        The goal is to count how many free places and hunters there are in each halve:
        left halve, right halve, up halve, down halve.
        :param coords : tuple (x,y)
        :return: nothing.
        """
        x_value, y_value = coords[X_COORD] - 1, coords[Y_COORD] - 1
        if self.board[x_value][y_value] == self.HUNTER_SIGN:
            if self._is_coord_in_left_halve(x_value, y_value):
                self.hunters_left_halve += 1
            else:
                self.hunters_right_halve += 1

            if self._is_coord_in_up_halve(x_value, y_value):
                self.hunters_up_halve += 1
            else:
                self.hunters_down_halve += 1

        else:  # self.board[x_value][y_value] == BOX_SIGN
            if self._is_coord_in_left_halve(x_value, y_value):
                self.boxes_left_halve += 1
            else:
                self.boxes_right_halve += 1

            if self._is_coord_in_up_halve(x_value, y_value):
                self.boxes_up_halve += 1
            else:
                self.boxes_down_halve += 1

    def update_free_seats_by_side_counter(self):
        each_side_size = (self.N * self.N) / 2
        self.free_seats_left_halve = each_side_size - self.hunters_left_halve - self.boxes_left_halve
        self.free_seats_right_halve = each_side_size - self.hunters_right_halve - self.boxes_right_halve
        self.free_seats_up_halve = each_side_size - self.hunters_up_halve - self.boxes_up_halve
        self.free_seats_down_halve = each_side_size - self.hunters_down_halve - self.boxes_down_halve

    def _is_coord_in_left_halve(self, x, y):
        return x - 1 < self.N / 2

    def _is_coord_in_up_halve(self, x, y):
        return y - 1 > self.N / 2
