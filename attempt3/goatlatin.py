from collections import deque

def string_to_goat(sent: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_queue = deque(sent)
    first_letter = sent[0]
    breakpoint()

if __name__ == '__main__':
    string_to_goat('I speak goat latin')