#! /usr/bin/python2.7
import re

def english_text_to_piglatin(paragraph):
    '''Return the piglatin equivalent of a single paragraph
    '''
    paras = paragraph.split('\n')
    try:
        return '\n'.join([english_paragraph_to_piglatin(para) for para in paras])
    except:
        print "The text is: " + paragraph
        raise

def english_paragraph_to_piglatin(paragraph):
    '''Return the piglatin equivalent of a single paragraph
    '''
    sentences = re.findall(r'(?:\d[,.!?]|[^,.!?])*(?:[,.!?]|$)', paragraph)[0:-1]
    try:
        return ''.join([english_sentence_to_piglatin(sentence) for sentence in sentences])
    except:
        print "The paragraph is: " + paragraph
        raise


def english_sentence_to_piglatin(line):
    '''Return the piglatin equivalent of a single sentence
    '''
    words = line.split(' ')
    try:
        return ' '.join([english_word_to_piglatin(word) for word in words])
    except:
        print "The line is: " + line
        raise


'''Return the piglatin equivalent of a single word
'''
def english_word_to_piglatin(word):
    # Check for empty strings
    if len(word) == 0:
        return ''

    # Check that the word starts with a letter
    if not word[0].isalpha():
        return word

    # Check for capitalization
    if word.istitle():
        cap_flag = True
        word = word.lower()
    else:
        cap_flag = False


    # check for special character (.,?!) at the end of the word
    special_char_flag = False
    last_char = ''
    if word[-1] in [',', '.','!', '?']:
        special_char_flag = True
        last_char = word[-1]
        word = word[0:-1]
        
    # Construct suffixes based on word capitalization
    vowel_suffix = 'way'
    consonant_suffix = 'ay'

    if _is_consonant(word[0]): # First letter is a consonant
        return_word = _consonant_word_to_piglatin(word) + consonant_suffix
    else: # First letter is a vowel
        return_word = word + vowel_suffix


    if special_char_flag:
        return_word = return_word + last_char
        
    if cap_flag:
        return return_word.title()
    else:
        return return_word


def _consonant_word_to_piglatin(word):
    '''Return piglatin equivalent of a word beginning with a
    consonant cluster'''
    def _rearrange_letters(word, cluster = ''):
        if len(word) == 0: # Needed when word contains only consonants
            return cluster
        elif not word[0].isalpha():
            raise ValueError, 'Unexpected character ' + word[0] + '. Aborting'
        elif _is_consonant(word[0]) and not word[0] == 'y' : # Add to consonant cluster and keep checking
            return _rearrange_letters(word[1:], cluster + word[0])

        else: # reached a vowel
            if word[1::] == cluster:
                return word
            else:
                return word + cluster

    return _rearrange_letters(word)


def _is_consonant(letter):
    '''Returns True if the letter is a consonant, otherwise
    return False'''
    return letter.isalpha() and letter.lower() not in ['a', 'e', 'i', 'o', 'u']
