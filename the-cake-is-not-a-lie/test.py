import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class CakeTestCase(unittest.TestCase):

    @unpack
    @data(
        ("abc", 1),
        ("abcdefabc", 1),
        ("abccbaabccba", 2),
        ("abcabcabcabc", 4)
    )
    def test_answer(self, input_string, expected):
        self.assertEquals(expected, solution.answer(input_string))


if __name__ == '__main__':
    unittest.main()
