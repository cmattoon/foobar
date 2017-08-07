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
        ),
        (# Case 3
            [ [1] ],
            [1, 1]
        )
    )
    @unpack
    def test_answer(self, m, exp):
        ##self.assertEquals(exp, solution.answer(m))
        pass
    
    @data(
        (1, [[1]]),
        (2, [
            [1, 0],
            [0, 1]
        ]),
        (3,
         [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]
         ]
        )
    )
    @unpack
    def test_idmatrix(self, n, exp):
        self.assertEquals(exp, solution.idmatrix(n))

    @data(
        (#Case 1
            [[1, 2],
             [3, 4]],

            [[4, 3],
             [2, 1]],

            [[-3, -1],
             [1, 3]]
        ),
        (# Case 2
            [[9, 8, 7],
             [6, 5, 4],
             [0.5, 0.25, 0.25]],
            
            [[0, 0, 1],
             [0, 1, 0],
             [1, 1, 2]],

            [[9, 8, 6],
             [6, 4, 4],
             [-0.5, -0.75, -1.75]]
        )
    )
    @unpack
    def test_msub(self, a, b, exp):
        self.assertEquals(exp, solution.msub(a, b))


    @data(
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
            ],
            [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]
            ]
        ),
        (
            [[0, 2, 3],
             [1, 0, 0],
             [0, 0, 0]],
            
            [[0, 2, 3],
             [1, 0, 0],
             [0, 0, 1]]
        )
    )
    @unpack
    def test_absorbing_states(self, m1, m2):
        self.assertEquals(m2, solution.add_absorbing_states(m1))


if __name__ == '__main__':
    unittest.main()
