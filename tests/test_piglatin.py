import unittest
from src import piglatin

class TestStringMethods(unittest.TestCase):

    def test_simple(self):

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

        for english, pig_latin in examples.iteritems():
            self.assertEqual(
                piglatin.english_text_to_piglatin(english),
                pig_latin
            )

if __name__ == '__main__':
    unittest.main()
