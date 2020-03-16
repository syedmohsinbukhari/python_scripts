"""
Description: This script converts a string to a number. This string contains
number of stars of each task. Number of stars represent complexity of the task.

For example,
324 means that complexity of first task is 3 stars, second task is 2 starts and
third task is 4 stars.

Each star increases time required to complete that task by twice as much,
starting from 1 star complexity.

1 star = 1 hour
2 star = 2 hours
3 star = 4 hours
4 star = 8 hours
5 star = 16 hours
and so on

Author: syedmohsinbukhari@googlemail.com
"""
import sys


def main():
    if len(sys.argv) > 2:
        raise(TypeError("Please provide valid number of arguments"))

    star_string = sys.argv[1]
    total_hours = 0
    for c in star_string:
        num_stars = int(c)
        total_hours += 2**(num_stars-1)

    print(f"Total hours: {total_hours}")


main()

