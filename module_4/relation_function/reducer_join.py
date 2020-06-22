import sys


def reducer():
    for line in sys.stdin:
        cnt, value = line.strip().split('\t')
        yield cnt.strip()


def main():
    set_my = set()
    for i in reducer():
        set_my.add(i)

    for i in sorted(set_my):
        print(i)


if __name__ == '__main__':
    main()