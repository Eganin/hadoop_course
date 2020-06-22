import sys


def mapper():
    for line in sys.stdin:
        cnt, values = line.strip().split('\t')
        emit(cnt, values.strip().split(','))


def emit(key, values):
    for value in values:
        print(f'{key},{value}\t1')


if __name__ == '__main__':
    mapper()
