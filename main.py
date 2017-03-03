#! /usr/bin/python2.7

from src import piglatin

if __name__ == '__main__':
    '''Take a word from command line'''
    englishway = raw_input('Englishway exttay: ')
    
    igpay = piglatin.english_text_to_piglatin(englishway)
    print 'English: ', englishway
    print 'Piglatin:', igpay

