#! /usr/bin/python2.7

from src import piglatin
import argparse

def regular_input():
    '''Take a word from command line'''
    return raw_input('Input English: ')

def file_input(myfile):

    with open(myfile, 'r') as f:
        return f.read()

def doStuff(englishway):

    igpay = piglatin.english_text_to_piglatin(englishway)
    print 'English: ', englishway
    print 'Piglatin:', igpay

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Translate some English.')
    parser.add_argument(
        '--file',
        default = False,
        type = str,
        help = 'Read text from file'
    )

    args = parser.parse_args()


    if args.file:
        text = file_input(args.file)
    else:
        text = regular_input()

    doStuff(text)
