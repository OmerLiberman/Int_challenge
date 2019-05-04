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
        # the number of boxes and hunters in each part of the board
        self.boxes, self.hunters = [], []

    # ------------ even size board methods ------------ #
    def split_boxes_hunters_when_size_is_even(self, array_of_boxes_placed_coords, array_of_hunters_placed_coords):
        """
        A B
        D C
        :param array_of_boxes_placed_coords:
        :param array_of_hunters_placed_coords:
        :return:
        """
        boxes_a, hunters_a, boxes_b, hunters_b = 0, 0, 0, 0
        boxes_c, hunters_c, boxes_d, hunters_d = 0, 0, 0, 0

        for box in array_of_boxes_placed_coords:
            part_box_belongs_to = self._part_of_even_size_board_which_coords_in(box)
            if part_box_belongs_to == 'a':
                boxes_a += 1
            if part_box_belongs_to == 'b':
                boxes_b += 1
            if part_box_belongs_to == 'c':
                boxes_c += 1
            if part_box_belongs_to == 'd':  # == 'd'
                boxes_d += 1

        for hunter in array_of_hunters_placed_coords:
            part_box_belongs_to = self._part_of_even_size_board_which_coords_in(hunter)
            if part_box_belongs_to == 'a':
                hunters_a += 1
            if part_box_belongs_to == 'b':
                hunters_b += 1
            if part_box_belongs_to == 'c':
                hunters_c += 1
            if part_box_belongs_to == 'd':  # == 'd'
                hunters_d += 1

        self.boxes = [boxes_a, boxes_b, boxes_c, boxes_d]
        self.hunters = [hunters_a, hunters_b, hunters_c, hunters_d]

    def _part_of_even_size_board_which_coords_in(self, coords):
        """
        A B
        D C
        :param coords:
        :return:
        """
        x, y = coords[X_COORD], coords[Y_COORD]
        mid = self.N / 2
        if y <= mid:
            if x <= mid:
                return 'd'
            else:  # x > mid
                return 'c'
        else:  # y > mid
            if x <= mid:
                return 'a'
            else:  # x > mid
                return 'b'

    # ------------ odd size board methods ------------ #
    def split_boxes_hunters_when_size_is_odd(self, array_of_boxes_placed_coords, array_of_hunters_placed_coords):
        """
        A E B
        H I F
        D G C
        :param array_of_boxes_placed_coords:
        :param array_of_hunters_placed_coords:
        :return:
        """
        boxes_a, hunters_a, boxes_b, hunters_b = 0, 0, 0, 0
        boxes_c, hunters_c, boxes_d, hunters_d = 0, 0, 0, 0
        boxes_e, hunters_e, boxes_f, hunters_f = 0, 0, 0, 0
        boxes_g, hunters_g, boxes_h, hunters_h = 0, 0, 0, 0
        boxes_center, hunters_center = 0, 0

        for box in array_of_boxes_placed_coords:
            part_box_belongs_to = self._part_of_odd_size_board_which_coords_in(box)
            if part_box_belongs_to == 'a':
                boxes_a += 1
            if part_box_belongs_to == 'b':
                boxes_b += 1
            if part_box_belongs_to == 'c':
                boxes_c += 1
            if part_box_belongs_to == 'd':
                boxes_d += 1
            if part_box_belongs_to == 'e':
                boxes_e += 1
            if part_box_belongs_to == 'f':
                boxes_f += 1
            if part_box_belongs_to == 'g':
                boxes_g += 1
            if part_box_belongs_to == 'h':
                boxes_h += 1
            if part_box_belongs_to == 'i':
                boxes_center += 1

        for hunter in array_of_hunters_placed_coords:
            part_hunter_belongs_to = self._part_of_odd_size_board_which_coords_in(hunter)
            if part_hunter_belongs_to == 'a':
                hunters_a += 1
            if part_hunter_belongs_to == 'b':
                hunters_b += 1
            if part_hunter_belongs_to == 'c':
                hunters_c += 1
            if part_hunter_belongs_to == 'd':
                hunters_d += 1
            if part_hunter_belongs_to == 'e':
                hunters_e += 1
            if part_hunter_belongs_to == 'f':
                hunters_f += 1
            if part_hunter_belongs_to == 'g':
                hunters_g += 1
            if part_hunter_belongs_to == 'h':
                hunters_h += 1
            if part_hunter_belongs_to == 'i':
                hunters_center += 1

        self.boxes = [boxes_a, boxes_b, boxes_c, boxes_d, boxes_e, boxes_f, boxes_g, boxes_h, boxes_center]
        self.hunters = [hunters_a, hunters_b, hunters_c, hunters_d, hunters_e, hunters_f, hunters_g, hunters_h,
                        hunters_center]

    def _part_of_odd_size_board_which_coords_in(self, coords):
        """
        A E B
        H I F
        D G C
        :param coords:
        :return:
        """
        x, y = coords[X_COORD], coords[Y_COORD]
        mid = (self.N + 1) / 2
        if y < mid:
            if x < mid:
                return 'd'
            if x == mid:
                return 'g'
            else:  # x > mid
                return 'c'
        if y > mid:
            if x < mid:
                return 'a'
            if x == mid:
                return 'e'
            else:  # x > mid
                return 'b'
        else:  # y = mid
            if x < mid:
                return 'h'
            if x > mid:
                return 'f'
            else:  # x = mid
                return 'i'
