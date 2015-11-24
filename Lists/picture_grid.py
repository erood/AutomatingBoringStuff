#! python3
# picture_grid.py - this program prints a picture character stored in a multidimensional array.

__author__ = 'm'


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for x_position in range(len(grid[0])):
        for y_position in range(len(grid)):
            print(grid[y_position][x_position], end="")
        print()

if __name__ == "__main__":
    main()
