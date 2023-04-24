import unittest
from W2H2 import Choice, choices, get_comp_choice

class TestChoice(unittest.TestCase):
    '''
    Testing class Choice in RPS game.
    '''

    @classmethod
    def setUpClass(cls) -> None:
        # https://stackoverflow.com/a/34065561/10474024
        # https://dzone.com/articles/python-unit-testing-one-time-initialization
        # return super().setUpClass()
        cls.choice_obj = Choice()

    def test_Choice_init(self):
        '''
        Testing instantiation.
        '''
        self.assertEqual(TestChoice.choice_obj.choice, 0)
    
    def test_Choice_setter_int_good(self):
        '''
        Testing Choice setter (INT - good)
        '''
        TestChoice.choice_obj.choice = 1
        self.assertEqual(TestChoice.choice_obj.choice, 1)
        TestChoice.choice_obj.choice = 2
        self.assertEqual(TestChoice.choice_obj.choice, 2)
        TestChoice.choice_obj.choice = 3
        self.assertEqual(TestChoice.choice_obj.choice, 3)
    
    def test_Choice_setter_int_bad(self):
        '''
        Testing Choice setter (INT - bad)
        '''
        try:
            TestChoice.choice_obj.choice = 0
        except Exception as err:
            self.assertIsInstance(err, ValueError)
    
    def test_Choice_setter_str_good(self):
        '''
        Testing Choice setter (STR - good)
        '''
        TestChoice.choice_obj.choice = '1'
        self.assertEqual(TestChoice.choice_obj.choice, 1)
    
    def test_Choice_setter_str_bad(self):
        '''
        Testing Choice setter (STR - bad)
        '''
        try:
            TestChoice.choice_obj.choice = 'random'
        except Exception as err:
            self.assertIsInstance(err, TypeError)
    
    def test_Choice_setter_none(self):
        '''
        Testing Choice setter (None)
        '''
        try:
            TestChoice.choice_obj.choice = None
        except Exception as err:
            self.assertIsInstance(err, TypeError)
    
    # def test_Choice_input(self):
    #     '''
    #     Testing command line input function
    #     '''

    #     pass

class TestCompChoice(unittest.TestCase):
    '''
    Testing class Choice in RPS game.
    '''
    def test_getCompChoice(self):
        '''
        Testing computer choice
        '''
        comp = get_comp_choice()
        self.assertIn(comp, list(range(1, len(choices.keys())+1)))

if __name__ == '__main__':
    unittest.main()