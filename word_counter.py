#!/usr/bin/env python3

from collections import Counter, defaultdict

def load_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    lines = load_file('Latin-Lipsum.txt')
    word_count = Counter()
    for line in lines:
        word_count += Counter(line.split())
    print("As a counter")
    print(word_count)
    print(word_count.most_common(5))