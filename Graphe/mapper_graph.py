import sys


def main():
    for line in sys.stdin:
        print(line.strip())

        head, weight, nodes = line.strip().split('\t')
        adjuency_lst = nodes[1:-1].split(',')
        if adjuency_lst != ['']:
            weight = int(weight) + 1 if weight != 'INF' else str(weight)
            for i in adjuency_lst:
                print(str(i) + '\t' + str(weight) + '\t' + '{}')


if __name__ == '__main__':
    main()