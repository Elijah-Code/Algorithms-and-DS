"""
Cracking the code interview - 17.22
"""

import english_words

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
words = set(english_words.english_words_alpha_set)

def change_letter(s, ix, new):
    return s[:ix] + new + s[ix+1:]

def word_transformer(start_word, end_word, exclude_words=set()):
    if start_word not in words or start_word in exclude_words:
        return False
    if start_word == end_word:
        return True
    
    exclude_words.add(start_word)

    for letter_ix in range(len(start_word)):
        for letter in alphabet:
            transformed_word = change_letter(start_word, letter_ix, letter)
            if word_transformer(transformed_word, end_word, exclude_words):
                return True
            
            


