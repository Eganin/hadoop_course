import sys


def mapper():
    for line in sys.stdin:
        emit(line.strip().split(',')[0])


def emit(value):
    print(f'{value}\t1')


if __name__ == '__main':
    mapper()
