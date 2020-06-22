import sys
from collections import defaultdict


def mapper():
    sum_ = defaultdict(int)
    cnt_ = defaultdict(int)

    for line in sys.stdin:
        key, val = line.split('\t')
        second, users = val.split(';')
        sum_[key] += int(second)
        cnt_[key] += int(users)

    for key in cnt_:
        avg = str(str(sum_[key]) + ';' + str(cnt_[key]))
        emit(key, avg)


def emit(key, value):
    print(f'{key}\t{value}')


if __name__ == '__main__':
    mapper()
