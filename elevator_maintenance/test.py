import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class ElevatorTestCase(unittest.TestCase):

    @data(
        (["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]),
        (["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"], ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"])
    )
    @unpack
    def test_answer(self, lst, expected):
        self.assertEqual(expected, solution.answer(lst))


if __name__ == '__main__':
    unittest.main()
