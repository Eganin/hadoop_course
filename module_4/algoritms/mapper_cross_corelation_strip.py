import sys
from collections import Counter


def mapper():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            stripe = Counter(word2 for word2 in words if word2 != word)

            print(word, ','.join(f"{key}:{value}" for key, value in stripe.items()), sep='\t')


if __name__ == '__main__':
    mapper()
