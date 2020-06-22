import sys


def mapper() -> None:
    for line in sys.stdin:
        for token in line.strip().split():
            if token:
                emit(token)


def emit(token) -> None:
    print(token + '\t1')


if __name__ == '__main__':
    mapper()
