import sys


def reducer() -> None:
    lastKey, sum = None, 0
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        if lastKey and lastKey != key:
            emit(lastKey, sum)
            lastKey, sum = key, int(value)
        else:
            lastKey, sum = key, sum + int(value)
    if lastKey:
        emit(lastKey, sum)


def emit(lastkey, sum):
    print(f'{lastkey}\t{sum}')


if __name__ == '__main__':
    reducer()
