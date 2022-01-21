import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "nenya"
        result = cap.cap_func(text)
        self.assertEqual(result,"Nenya")

    def test_multiple_words(self):
        text ="raki ve nenya"
        result = cap.cap_func(text)
        self.assertEqual(result,"Raki Ve Nenya")


if __name__ == '__main__':
    unittest.main()