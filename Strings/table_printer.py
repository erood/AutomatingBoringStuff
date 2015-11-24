#! python3.4
# table_printer.py - takes a lists of lists of strings and displays it in a well-organized
# table with each column right-justified.
__author__ = 'm'

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def get_max_column_widths_of_a_table(table):
    col_widths = []
    for column in table:
        col_widths.append(max([len(e) for e in column]))

    return col_widths


def print_table(table):
    col_widths = get_max_column_widths_of_a_table(table)

    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j]), end=' ')
        print()


def main():
    print_table(table_data)


if __name__ == "__main__":
    main()
