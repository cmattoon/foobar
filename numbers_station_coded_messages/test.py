import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class NSCMTestCase(unittest.TestCase):

    @data(
        ([0], 0, [0,0]),
        ([0], 1, [-1,-1]),
        ([0,0,1,0,0,1,0,1], 1, [2,2]),
        ([4,3,5,7,8],12, [0,2]),
        ([4,3,10,2,8], 12, [2,3]),
        ([1,2,3,4], 15, [-1,-1]),
        ([1,2,15,3,4], 15, [0,2]),
        ([1,2,16,3,4], 15, [-1,-1]),
        ([1,3,3,7], 6, [1,2]),
        ([1,2,3,99,88,77,3,2,1,7], 6, [0, 2]),#Not the 2nd one
        ([6,5,6,7,11], 11, [0,1]),
        ([5,6,5,6,5,6,5,6], 11, [0,1]),
        ([11, 5, 6], 11, [0, 0]),
        ([10,0,1], 11, [0,2]),
        ([1,2,3], 6, [0,2])
    )
    @unpack
    def test_answer(self, l, t, expected):
        self.assertEqual(expected, solution.answer(l, t))


if __name__ == '__main__':
    unittest.main()
