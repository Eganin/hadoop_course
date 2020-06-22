import sys


def convert(value):
    if value == '{}':
        return []

    else:
        return value[1:-1].split(',')


def main():
    for line in sys.stdin:
        head, pagerank, adjacency = line.strip().split('\t')
        adjacency_lst = convert(adjacency)
        try:
            pg = float(pagerank) / len(adjacency_lst)

        except ZeroDivisionError:
            continue

        print(line.strip())
        for value in adjacency_lst:
            print('%s\t%.3f\t{}' % (value, pg))


if __name__ == '__main__':
    main()