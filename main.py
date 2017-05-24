#! /usr/bin/python2.7
# coding: utf-8

from src import piglatin
import argparse

def regular_input():
    '''Take text from command line, STDIN
    Input: NA
    Return: string from command line.'''
    return raw_input('Input English: ')

def file_input(myfile):
    '''Read text from file.
    Input myfile: path to file with text.
    Return: string found in myfile.'''

    with open(myfile, 'r') as f:
        return f.read()

def doStuff(englishway):
    '''Main function to call with string. Does the pigtranslation.
    Input englishway: string with english text to translate.
    Return NA.'''

    igpay = piglatin.english_text_to_piglatin(englishway)
    print 'English: ', englishway
    print 'Piglatin:', igpay

if __name__ == '__main__':

    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='Translate some English.')
    parser.add_argument(
        '--file',
        default = False,
        type = str,
        help = 'Read text from file'
    )

    args = parser.parse_args()

    # Choose if read from command line or from file.
    if args.file:
        text = file_input(args.file)
    else:
        text = regular_input()

    doStuff(text)
