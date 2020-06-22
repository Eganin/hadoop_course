import sys
from collections import defaultdict


def reducer():
    sum_ = defaultdict(int)
    cnt_ = defaultdict(int)

    for line in sys.stdin:
        key, val = line.split('\t')
        sum_[key] += int(val)
        cnt_[key] += 1

    for key in cnt_:
        avg = int(sum_[key] / cnt_[key])
        emit(key, avg)


def emit(key, value):
    print(f'{key}\t{value}')


if __name__ == '__main__':
    reducer()
