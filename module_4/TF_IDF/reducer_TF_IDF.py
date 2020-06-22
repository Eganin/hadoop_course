import sys
from collections import defaultdict


def reducer():
    my_dict = defaultdict(int)
    for line in sys.stdin:
        value, key = line.strip().split('\t')
        name, doc_num = value.strip().split('#')
        my_dict[str(str(name) + '_' + str(doc_num))] += int(key)

    for k, v in my_dict.items():
        print(*k.strip().split('_'), v, sep='\t')


reducer()