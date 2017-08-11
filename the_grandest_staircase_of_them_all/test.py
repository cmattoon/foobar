import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class SolutionTestCase(unittest.TestCase):

    @data(
        (3, 1),
        (200, 487067745)
    )
    @unpack
    def test_answer(self, n, exp):
        self.assertEquals(exp, solution.answer(n))


if __name__ == '__main__':
    unittest.main()
