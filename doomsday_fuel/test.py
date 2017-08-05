import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class SolutionTestCase(unittest.TestCase):

    # @data(
    #     (# Case 1
    #         [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    #         [[1,2],[1,2],[3,4]],
    #         [[12, 18], [27, 42], [42, 66], [57, 90]]
    #     ),
    # )
    # @unpack
    # def test_matmul(self, m1, m2, m3):
    #     self.assertEqual(m3, solution.matmul(m1, m2))

    @data(
        (# Case 1
            [
                [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            [7, 6, 8, 21]
        ),
        (# Case 2
            [
                [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ],
            [0, 3, 2, 9, 14]
        )
    )
    @unpack
    def test_answer(self, m, exp):
        self.assertEquals(exp, solution.answer(m))

        
if __name__ == '__main__':
    unittest.main()
