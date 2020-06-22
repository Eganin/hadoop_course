import sys

def mapper():
    for line in sys.stdin:
        name , doc_num , cnt = line.strip().split('\t')
        print(name + '\t' +doc_num+';'+cnt+';'+str(1))

mapper()