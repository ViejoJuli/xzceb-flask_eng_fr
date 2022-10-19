import unittest
import sys
sys.path.append("/home/project/xzceb-flask_eng_fr/final_project/machinetranslation")
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertIsNotNone(french_to_english("Bonjour"))
        self.assertEqual(french_to_english("Bonjour"),"Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNotNone(english_to_french("Hello"))
        self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__ == "__main__":
    unittest.main()