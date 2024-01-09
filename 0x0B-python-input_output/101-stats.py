#!/usr/bin/python3
"""Reads from standard input and computes metrics.
"""


import sys


def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
    - total_size (int): Total file size.
    - status_codes (dict): Dictionary containing the count of each status code.
    """
    print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parses a line and extracts information.

    Args:
    - line (str): Input line to be parsed.

    Returns:
    - tuple: Tuple containing status code and file size.
    """
    parts = line.split()
    return (int(parts[-2]), int(parts[-1]))


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
