import sys


def reducer():
    H = {}
    for line in sys.stdin:
        value, key = line.strip().split('\t')
        H.setdefault(key, set()).add(value)

    for k, v in H.items():
        emit(k, v)


def emit(key, value):
    print(f'{key}\t{value}')


if __name__ == '__main__':
    reducer()
