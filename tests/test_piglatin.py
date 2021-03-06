# coding: utf-8

import unittest
from src import piglatin

import main
import os

class TestStringMethods(unittest.TestCase):

    def test_read_from_file(self):

        path = os.path.dirname(__file__)

        filepath = os.sep.join([path, 'testFile.txt'])

        value = main.file_input(filepath)

        self.assertEqual(value, 'This is a test.\n')

    def test_single_words(self):

        examples = {
            "pig" : "igpay",
            "Latin" : "Atinlay",
            "banana" : "ananabay",
            "trash" : "ashtray",
            "happy" : "appyhay",
            "duck" : "uckday",
            "glove" : "oveglay",
            "latin" : "atinlay",
            "dopest" : "opestday",
            "me" : "emay",
            "too" : "ootay",
            "thanks" : "anksthay",
            "will" : "illway",
            "moist" : "oistmay",
            "wet" : "etway",
            # When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing.[7]
            "cheers" : "eerschay",
            "shesh" : "eshay",
            "smile" : "ilesmay",
            # For words that begin with vowel sounds, one just adds "way" to the end. Examples are:
            "eat" : "eatway",
            "omelet" : "omeletway",
            "are" : "areway",
            "egg" : "eggway"}

        output = []
        ref = []
        for english, pig_latin in examples.iteritems():
            output.append(piglatin.english_text_to_piglatin(english))
            ref.append( pig_latin)

        self.maxDiff = None
        # Test everything at once
        self.assertEqual(tuple(output),tuple(ref))

    def test_phrases(self):

        examples = [
            "Hello",
            "Ellohay",
            "Please",
            "Easeplay",
            # "What time is it?",
            # "Hatway imetay ishay ithay?",
            # "How is the weather?",
            # "Owhay ishay hetay pathway?",
            # "How are you?",
            # "Owhay arehay ouyay?",
            # "What is your name?",
            # "Hatway ishay ouryay amenay?",
            # "Thank you",
            # "Hanktay ouyay",
            # "You are welcome",
            # "Ouyay arehay elcomeway",
            # "Good night",
            # "Oodgay ightnay",
            # "Who is that?",
            # "Howay ishay hattay?",
            # "Where are you going?",
            # "Hereway arehay ouyay oinggay?",
            # "I don’t want to",
            # "Ihay on’tday antway otay",
            # "Do you understand?",
            # "Oday ouyay underway tandsay?",
            # "Where do you come from?",
            # "Hereway oday ouyay omecay romfay?",
            # "Whisper it to me",
            # "Hisperway ithay otay emay",
            # "Can you speak Pig Latin?",
            # "Ancay ouyay peaksay igpay atinlay?",
            # "What are you talking about?",
            # "Hatway arehay ouyay alkingtay aboutway?",
            # "What is the password?",
            # "Hatway ishay hetay asspay ordway?",
            # "What is the answer for...?",
            # "Hatway ishay hetay answerway orfay...?",
            # "Why are you doing that?",
            # "Hyway arehay ouyay oingday hattay?",
            # "I’m in trouble",
            # "I’mhay inhay roubletay",
            # "Hide the gift now",
            # "Idehay hetay iftgay ownay",
            # "Wait until she leaves",
            # "Aitway untilway hesay eaveslay",
            # "Bring it tomorrow",
            # "Ringbay ithay omorrowtay",
            # "Follow me",
            # "Ollowfay emay",
            # "Don’t leave",
            # "On’tday eavelay",
            # "Go now",
            # "Ogay ownay",
            # "I don’t like this",
            # "Iay on’tday ikelay histay",
            # "Why is he here?",
            # "Hyway ishay ehay erehay?",
            # "What is her name?",
            # "Hatway ishay erhay amenay?",
            # "Do you have the homework?",
            # "Oday ouyay avehay hetay omehay orkway?",
            # "He is so cute",
            # "Ehay ishay osay utecay",
            # "Call me",
            # "Allcay emay",
            # "Here is my number",
            # "Erehay isway ymay umbernay",
            # "Don’t tell them",
            # "On’tday elltay hemtay",
            # "This is a secret",
            # "Isthay isway away egrets",
            # "Please remind me",
            # "Easeplay emindray emay",
            # "No way",
            # "Onay ayway"
        ]

        inp = examples[0::2]
        ref = examples[1::2]
        out = [piglatin.english_text_to_piglatin(eng) for eng in inp]

        self.maxDiff = None
        self.assertTupleEqual(tuple(out),tuple(ref))

if __name__ == '__main__':
    unittest.main()
