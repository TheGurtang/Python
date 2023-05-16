# here we begin our testing file with importing a built-in testing function

import unittest                    # here we import the in-built testing library
import Tested_File_1               # here we import the file which is subjected to testing


class TestMain(unittest.TestCase):             # we create calss, chosing its name randomly, but (unittest.TestCase) - obligatory
    def test_do_stuff(self):                   # here we create a testing function with (self) - inheritance
        num = 10                               # we introduce variable related to the tested function
        result = Tested_File_1.do_stuff(num)        # we insert a scenario for a result by spotting the name of tested file and the name of tested function
        self.assertEqual(result, 15)                # here we assign assertEqual() function where we show waht result SHOULD BE if the fucntion works correctly

    def test_get_word(self):
        a = 'fork'
        b = a
        self.assertIs('fork', b)               # here we use assetIs(arg, arg) which tests if tested values match each other

    def test_seq_n(self):
        seq = 'There is an interesting text for working over'
        seq_2 = 'is'
        self.assertIn(seq_2, 'There is an interesting text for working over')    # assertIn(looked arg, given arg) is used in testing scenario to check if one arg is in another one





unittest.main()                                 # this command launch the test-scenario and should look like this unittest.main()

