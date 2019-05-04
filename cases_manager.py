from case import Case


class CasesManager:
    def __init__(self, num_of_cases):
        self.num_of_cases = num_of_cases
        self.cases = []

    def add_case(self, n, b, h, array_of_lines):
        coordinates_array = self._convert_coordinates_lines_to_tuples(array_of_lines)
        boxes_coordinates = coordinates_array[:b]
        hunters_coordinates = coordinates_array[b:]
        new_case = Case(n, b, h, boxes_coordinates, hunters_coordinates)
        self.cases.append(new_case)

    def _convert_coordinates_lines_to_tuples(self, lines):
        array_of_tuples = []
        for line in lines:
            x_str, y_str = line.split()
            tup = int(x_str), int(y_str)
            array_of_tuples.append(tup)
        return array_of_tuples

    def solve_all_cases(self):
        solves = []
        for case in self.cases:
            solve = case.solve()
            solves.append(solve)
        self._print_out_cases_solves(solves)

    def _print_out_cases_solves(self, solves):
        for solve_number in range(len(solves)):
            print("Case #" + str(solve_number + 1) + ": " + str(solves[solve_number]))
