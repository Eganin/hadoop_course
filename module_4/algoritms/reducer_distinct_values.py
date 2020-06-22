import sys


def reducer():
    output = set()
    for line in sys.stdin:
        value, _ = line.strip().split('\t')
        output.add(value)

    emit(output)


def emit(output):
    for i in sorted(output):
        print(i)


if __name__ == '__main__':
    reducer()
