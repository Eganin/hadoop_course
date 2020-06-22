import sys

prev_node = ''
sum_weight = 0
prev_adjacency = '{}'

for line in sys.stdin:
    node, weight, adjacency_str = line.strip().split('\t')

    if not prev_node:
        if adjacency_str == '{}':
            sum_weight += float(weight)
        else:
            prev_adjacency = adjacency_str

    elif node == prev_node:
        if adjacency_str == '{}':
            sum_weight += float(weight)
        else:
            prev_adjacency = adjacency_str

    else:
        if prev_adjacency == '{}':
            print('%s\t0\t%s' % (prev_node, prev_adjacency))
        else:
            print('%s\t%.3f\t%s' % (prev_node, sum_weight, prev_adjacency))

        if adjacency_str == '{}':
            sum_weight = float(weight)
        else:
            sum_weight = 0
            prev_adjacency = adjacency_str

    prev_node = node

if prev_adjacency == '{}':
    print('%s\t0\t%s' % (prev_node, prev_adjacency))
else:
    print('%s\t%.3f\t%s' % (prev_node, sum_weight, prev_adjacency))