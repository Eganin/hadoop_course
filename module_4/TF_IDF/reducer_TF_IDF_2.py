import sys
from collections import defaultdict


def process(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        if v < 2:
            pass
        else:
            new_dict[k] = v

    return new_dict


def reducer():
    cache = defaultdict(int)
    res = []
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        cache[key] += 1
        res.append((key, value))

    double_values = process(cache)
    for k, v in res:
        one, two, three = v.split(';')
        if k in double_values:
            print(str(k) + '#' + str(one) + '\t' + str(two) + '\t' + str(double_values[k]))

        else:
            print(str(k) + '#' + str(one) + '\t' + str(two) + '\t' + str(three))


if __name__ == '__main__':
    reducer()