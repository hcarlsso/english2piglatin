#! /usr/bin/python2.7

'''Takes a single word as input and returns its 
   piglatin equivalent'''
def from_english_word(word):
    if is_consonant(word[0]): # First letter is a consonant
        if is_consonant(word[1]): # Second letter is a consonant too
            return word[2:-1] + word[-1] + word[0:2] + 'ay'
        else:
            return word[1:-1] + word[-1] + word[0] + 'ay'
    else: # First letter is a vowel
        return word + 'way'

'''Returns True if the letter is consonant, otherwise
   return False'''
def is_consonant(letter):
    if letter not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
