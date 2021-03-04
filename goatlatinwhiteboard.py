#!/usr/bin/env python3 

def string_to_goat_latin(string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_str_list = []
    counter = 1
    split_sent = string.split(' ')
    for word in split_sent:
        if word[0].lower() in vowels:
            word = word + 'ma'
        else:
            first_letter = word[0]
            word = word[1:] + first_letter + 'ma'
        ending_letter = counter * 'a'
        new_str_list.append(word + ending_letter)
        counter += 1
    print(" ".join(new_str_list))
    
string_to_goat_latin('I speak Goat Latin')