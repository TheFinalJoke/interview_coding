#!/usr/bin/env python3

from collections import Counter
def load_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

def word_count():
    pass

if __name__ == "__main__":
    lines = load_file('Latin-Lipsum.txt')
    word_count = {}
    import pdb; pdb.set_trace()
    for line in lines:
        for word in line:
            pass
