from board import Board


class Case:
    NO_SOLVE = -1

    def __init__(self, n, b, h, boxes_coords, hunters_coords):
        self.is_size_even = (n % 2 == 0)
        self.board = Board(n, b, h, self.is_size_even)
        self.board.place_boxes_and_hunters(boxes_coords, hunters_coords)

    def solve(self):
        if self.is_size_even:
            self._solve_even_size_board()
        # else:
        #     self._solve_odd_size_board()

    def _solve_even_size_board(self):
        """
        the board looks like :
        A B
        D C
        - elaboration about this method is in the readme.
        :return: the number of hunters can be added to the board but it is still stable.
        """
        # hunt_ext_a -> hunters can be added to quarter A (see documentation)
        hunt_ext_a, hunt_ext_b, hunt_ext_c, hunt_ext_d = 0, 0, 0, 0
        # q_a_data -> quarter A data -> num of empty cells, num of hunters]
        q_a_data, q_b_data, q_d_data, q_c_data = self._split_board_to_four()
        hunt_ext_a, hunt_ext_c = self._solve_equation(hunt_ext_a, q_a_data[0], hunt_ext_c,
                                                      q_c_data[0],
                                                      q_c_data[1] - q_a_data[1])
        hunt_ext_d, hunt_ext_b = self._solve_equation(hunt_ext_d, q_d_data[0], hunt_ext_b,
                                                      q_b_data[0],
                                                      q_b_data[1] - q_d_data[1])
        if hunt_ext_a > self.NO_SOLVE and hunt_ext_b > self.NO_SOLVE and \
                hunt_ext_c > self.NO_SOLVE and hunt_ext_d > self.NO_SOLVE:
            return hunt_ext_a + hunt_ext_b + hunt_ext_c + hunt_ext_d
        return self.NO_SOLVE

    # def _solve_odd_size_board(self):
    #     return 0

    def _split_board_to_four(self):
        """
        Get the [num of empty cells, num of hunters] for each quarter of the board.
        the board looks like :
        A B
        D C
        :return:
        """
        half_of_n = int(self.board.N / 2)
        up_left_quarter_values = self._collect_data_on_part(0, half_of_n, 0, half_of_n)
        up_right_quarter_values = self._collect_data_on_part(half_of_n, self.board.N, 0, half_of_n)
        down_left_quarter_values = self._collect_data_on_part(0, half_of_n, half_of_n, self.board.N)
        down_right_quarter_values = self._collect_data_on_part(half_of_n, self.board.N, half_of_n, self.board.N)

        return up_left_quarter_values, up_right_quarter_values, down_left_quarter_values, down_right_quarter_values

    def _collect_data_on_part(self, x_start, x_end, y_start, y_end):
        """
        Trying to collect necessary data over specific part in the board.
        :param x_start, x_end, y_start, y_end: the limits of the part.
        :return: [num of empty cells, num of hunters]
        """
        free_seats_counter, hunters_counter = 0, 0
        for row in range(x_start, x_end):
            for column in range(y_start, y_end):
                if self.board.board[row][column] == self.board.HUNTER_SIGN:
                    hunters_counter += 1
                if self.board.board[row][column] == self.board.FREE_SEAT_SIGN:
                    free_seats_counter += 1
        return free_seats_counter, hunters_counter

    def _solve_equation(self, first_unknown, first_unknown_limit, second_unknown, second_unknown_limit, result):
        """
        Intend to solve the equation: first_unknown - second_unknown = result
        when : first_unknown <= first_unknown_limit
                second_unknown <= second_unknown_limit
        :param first_unknown, second_unknown:
        :param first_unknown_limit, second_unknown_limit:
        :return: tuple (first_unknown_value , second_unknown_value)
        """
        max_first, max_second = -1, -1
        for x in reversed(range(first_unknown_limit + 1)):
            for y in reversed(range(second_unknown_limit + 1)):
                if x - y == result and x + y > max_first + max_second:
                    max_first, max_second = x, y

        return max_first, max_second
