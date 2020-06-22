import sys
from collections import Counter


def mapper():
    for line in sys.stdin:
        my_dict = Counter(line.strip().split())
        for k, v in my_dict.items():
            emit(k, v)


def emit(key, value):
    print(f'{key}\t{value}')


if __name__ == '__main__':
    mapper()
