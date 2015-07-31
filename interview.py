__author__ = 'dlai'


def string_reverse(input_string):
    string_buffer = ""

    for(i=0; i<input_string.length; i++):
        string_buffer = input_string[i] + string_buffer


    return string_buffer



def is_anagram(word_one, word_two):

    letter_map = {}
    
    for c in word_one:
        if letter_map.has_key(c):
            letter_map[c] += 1
        else:
            letter_map[c] = 1

    for c in word_two:
