import os
import unittest

from W3H1_IO import print_to_file, read_n_match


# assertions:  https://docs.python.org/3/library/unittest.html#assert-methods
class TestIO(unittest.TestCase):
    """
    Testing IO functions from HW 3.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Class setup for whole of testing.
        """

        cls.file_name_r = "test_txt.txt"
        cls.str_to_match = "my love"
        cls.match_num = 2
        cls.str_to_fail = "error"
        cls.file_name_o = "test_output.txt"

        text_str = """Alas, my love has gone away.
I know not where he goes ...
But my love returns no more."""
        with open(TestIO.file_name_r, "w", encoding="UTF-8") as test_file:
            test_file.write(text_str)

    @classmethod
    def tearDownClass(cls):
        """
        Class to delete files created for testing.
        """
        try:
            os.remove(cls.file_name_r)
        except OSError:
            raise

        try:
            os.remove(cls.file_name_o)
        except OSError:
            raise

    def test_read_n_match_fail_none_returned(self):
        """
        Testing read and match function if returns None.
        """

        rtnd_list = read_n_match(TestIO.file_name_r, TestIO.str_to_match)
        self.assertNotIsInstance(
            rtnd_list, type(None), "This should never return None!"
        )

    # def test_read_n_match_fail(self):
    #     '''
    #     Testing read and match function if returns None.
    #     '''

    #     rtnd_list = read_n_match(TestIO.file_name, TestIO.str_to_match)
    #     self.assertNotIsInstance(rtnd_list, type(None),
    #           "This should never return None!")

    def test_read_n_match_success(self):
        """
        Testing working read and match function.
        Takes in:
        - file_in (string location of TXT file to read in)
        - pttrn (text to match matched)
        """

        # rtnd_list = read_n_match(TestIO.file_name_r, TestIO.str_to_match)
        TestIO.match_list = read_n_match(TestIO.file_name_r, TestIO.str_to_match)
        # self.assertIsInstance(rtnd_list, list,
        #       "Function did not return a list!")
        self.assertIsInstance(
            TestIO.match_list, list, "Function did not return a list!"
        )
        # self.assertEqual(len(rtnd_list),
        #       TestIO.match_num,"Incorrect number of lines found")
        self.assertEqual(
            len(TestIO.match_list),
            TestIO.match_num,
            "Incorrect number of lines found",
        )

    def test_print_to_file_no_match(self):
        """
        Testing print_to_file function. Takes in:
        - line_list (list of lines from read_n_match)
        - pttrn (text matched)
        - file_name='output.txt'
        """

        rtnd_list = read_n_match(TestIO.file_name_r, TestIO.str_to_fail)
        print_to_file(rtnd_list, TestIO.str_to_fail, TestIO.file_name_o)


if __name__ == "__main__":
    unittest.main()
