import sys


def generator():
    for line in sys.stdin:
        array = list(line.strip().split())
        for i in array:
            for j in array:
                if i != j:
                    yield (str(i) + ',' + str(j) + '\t' + str(1))

                else:
                    pass


def main():
    for i in generator():
        print(i)


if __name__ == '__main__':
    main()
