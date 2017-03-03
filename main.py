#! /usr/bin/python2.7

from src import piglatin

if __name__ == '__main__':
    '''Take a word from command line'''
    english_word = raw_input('Please enter a single English word:')
    
    piglatin_word = piglatin.from_english_word(english_word)
    print 'The piglatin for', english_word, 'is', piglatin_word

