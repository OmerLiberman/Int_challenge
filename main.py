# ----- IMPORTS ----- #
import sys
from cases_manager import CasesManager

# ----- CONSTANTS ----- #
EMPTY_STRING = ""
SPACE = " "


# ----- METHODS ----- #
def create_full_path(path):
    """
    this method receives parts of path to file and concatenate it.
    :param path: path to file
    :return: the concatenate path to the file
    """
    full_path = EMPTY_STRING
    for partial_string in path:
        full_path += partial_string + SPACE
    return full_path.strip()


def split_head_case_line(line):
    """
    breaks the line from the format "d d d" to n, b, h integers
    """
    n, b, h = line.split()
    n, b, h = int(n), int(b), int(h)
    return n, b, h


def read_file_to_case_dealer(path):
    """
    This method reads the given file to a case dealer object which handles the task.
    :return: cases_dealer object.
    """
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
    """
    main method.
    """
    path = create_full_path(sys.argv[1:])
    cases_dealer = read_file_to_case_dealer(path)
    cases_dealer.solve_all_cases()
    return 0


if __name__ == '__main__':
    main()
