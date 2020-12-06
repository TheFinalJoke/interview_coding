#!/usr/bin/env python3

def const_transform(word: str):
    letter = word[0]
    return word.replace(word[0], "") + letter + "ma"
def vowel_transform(word: str):
    return word + "ma"

def str_to_goat_latin(sent: str):
    new_list = []
    counter = 1
    split_str = sent.split(" ")
    vowel_list = ["a", "e", "i", "o", "u"]
    for word in split_str:
        if word[0].lower() in vowel_list:
            new_list.append(vowel_transform(word) + "a"*counter)
        else:
            new_list.append(const_transform(word) + "a"*counter)
        counter = counter + 1
    return " ".join(new_list)

if __name__ == "__main__":
   print(str_to_goat_latin("I speak Goat Latin")) 