import sys


def main():
    lastkey = None
    head_weight = []
    head_nodes = '{}'
    for line in sys.stdin:
        head, weight, nodes = line.strip().split('\t')

        if not lastkey:
            lastkey = head
            head_weight = weight
            head_nodes = nodes

        elif lastkey == head:
            try:
                head_weight = min(weight, head_weight)

            except:
                head_weight = 'INF'

            if nodes != '{}':
                head_nodes = nodes


        else:
            print(lastkey + '\t' + head_weight + '\t' + head_nodes)
            lastkey = head
            head_weight = weight
            head_nodes = nodes

    print(lastkey + '\t' + head_weight + '\t' + head_nodes)


if __name__ == '__main__':
    main()
