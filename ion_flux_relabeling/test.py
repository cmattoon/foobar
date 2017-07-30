import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class IonFluxTestCase(unittest.TestCase):

    @data(
        (3, [7,3,5,1], [-1,7,6,3]),
        (5, [19,14,28], [21,15,29])
    )
    @unpack
    def test_answer(self, h, q, exp):
        self.assertEqual(exp, solution.answer(h, q))


if __name__ == '__main__':
    unittest.main()
