import sys
from cases_manager import CasesManager

EMPTY_STRING = ""
SPACE = " "


def create_full_path(path):
    full_path = EMPTY_STRING
    for partial_string in path:
        full_path += partial_string + SPACE
    return full_path.strip()


def split_head_case_line(line):
    n, b, h = line.split()
    n, b, h = int(n), int(b), int(h)
    return n, b, h


def read_file_to_case_dealer(path):
    file = open(path, 'r')
    num_of_cases = int(file.readline())
    dealer = CasesManager(num_of_cases)
    cases_counter = 0
    while cases_counter < num_of_cases:
        case_lines = []
        n, b, h = split_head_case_line(file.readline())
        for i in range(b + h):
            case_lines.append(file.readline())
        dealer.add_case(n, b, h, case_lines)

        cases_counter += 1
    return dealer


def main():
    path = create_full_path(sys.argv[1:])
    cases_dealer = read_file_to_case_dealer(path)
    cases_dealer.solve_all_cases()
    return 0


if __name__ == '__main__':
    main()
