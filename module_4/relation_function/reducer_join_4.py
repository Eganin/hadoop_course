import sys


def mapper():
    one_set = set()
    two_set = []
    for line in sys.stdin:
        cnt, value = line.strip().split('\t')
        one_set.add(cnt)
        two_set.append(cnt)
    two_set = sorted(two_set)
    new_set = set()
    tw_set = set(two_set)

    for i in range(len(sorted(two_set))):
        if two_set[i] == two_set[i - 1]:
            new_set.add(two_set[i])

    res = tw_set - new_set
    for i in sorted(res):
        print(i)


if __name__ == '__main__':
    mapper()

