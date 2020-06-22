import sys


def mapper():
    one_set = set()
    two_set = set()
    for line in sys.stdin:
        cnt, value = line.strip().split('\t')
        if value == 'A':
            one_set.add(cnt)

        elif value == 'B':
            two_set.add(cnt)

    return list(one_set.difference(two_set))


def main():
    for i in sorted(mapper()):
        print(i)


if __name__ == '__main__':
    main()