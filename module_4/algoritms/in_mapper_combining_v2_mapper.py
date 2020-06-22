from collections import defaultdict
import sys


def mapper():
    cnt = defaultdict(int)
    for line in sys.stdin:
        for token in line.strip().split():
            cnt[token] += 1

    for key, val in cnt.items():
        emit(key, val)


def emit(key, value):
    print(f'{key}\t{value}')


if __name__ == '__main__':
    mapper()
