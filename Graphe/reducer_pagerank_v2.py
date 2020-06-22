import sys

N = 5
ALPHA = 0.1

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
            page_rank = ALPHA/N
        else:
            page_rank = ALPHA/N + (1 - ALPHA)*sum_weight

        print('%s\t%.3f\t%s' % (prev_node, page_rank, prev_adjacency))

        if adjacency_str == '{}':
            sum_weight = float(weight)
        else:
            sum_weight = 0
            prev_adjacency = adjacency_str

    prev_node = node

if prev_adjacency == '{}':
    page_rank = ALPHA/N
else:
    page_rank = ALPHA/N + (1 - ALPHA)*sum_weight

print('%s\t%.3f\t%s' % (prev_node, page_rank, prev_adjacency))

