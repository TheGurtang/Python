def just_do(text):
    return text.capitalize()

import unittest
import cap

class TestCap(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'dexter'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Dexter')

        def test_multiple_words(self):
            text = 'a mysterious group of murders'
            result = cap.just_do_it(text)
            self.assertEqual(result, 'A Mysterious Group Of Murders')



if __name__ == '__main__':
    unittest.main()
