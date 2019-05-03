from board import Board


# from sympy.solvers import solve, symbol, Eq


class Case:
    NO_SOLVE = -1

    def __init__(self, n, b, h, boxes_coords, hunters_coords):
        self.is_size_even = (n % 2 == 0)
        self.board = Board(n, b, h, self.is_size_even)
        self.board.split_boxes_hunters_when_size_is_even(boxes_coords, hunters_coords)

    def solve(self):
        if self.is_size_even:
            return self._solve_even_size_board()
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
        # q_a_data -> quarter A data -> num of empty cells, num of hunters]
        q_a_data, q_b_data, q_d_data, q_c_data = self._split_board_to_four()
        hunt_ext_a, hunt_ext_c = self._solve_equation(q_a_data[0], q_c_data[0], q_c_data[1] - q_a_data[1])
        hunt_ext_d, hunt_ext_b = self._solve_equation(q_d_data[0], q_b_data[0], q_b_data[1] - q_d_data[1])
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
        seats_in_quarter = self.board.N / 2 * self.board.N / 2
        a_quarter = seats_in_quarter - len(self.board.boxes_by_parts[0]) - len(
            self.board.hunters_by_part[0]), len(self.board.hunters_by_part[0])
        b_quarter = seats_in_quarter - len(self.board.boxes_by_parts[1]) - len(
            self.board.hunters_by_part[1]), len(self.board.hunters_by_part[1])
        d_quarter = seats_in_quarter - len(self.board.boxes_by_parts[3]) - len(
            self.board.hunters_by_part[3]), len(self.board.hunters_by_part[3])
        c_quarter = seats_in_quarter - len(self.board.boxes_by_parts[2]) - len(
            self.board.hunters_by_part[2]), len(self.board.hunters_by_part[2])

        return a_quarter, b_quarter, d_quarter, c_quarter

    def _solve_equation(self, first_unknown_limit, second_unknown_limit, result):
        """
        Intend to solve the equation: first_unknown - second_unknown = result
        when : first_unknown <= first_unknown_limit
                second_unknown <= second_unknown_limit
        :param first_unknown_limit, second_unknown_limit:
        :return: tuple (first_unknown_value , second_unknown_value)
        """
        max_first, max_second = -1, -1
        for x in reversed(range(int(first_unknown_limit + 1))):
            for y in reversed(range(int(second_unknown_limit + 1))):
                if x - y == result and x + y > max_first + max_second:
                    return x, y
        return max_first, max_second
