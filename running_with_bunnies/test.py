import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class AnswerTestCase(unittest.TestCase):

    @data(
        (# Case #1
            [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]
            ], # T
            3, # L
            [0,1] # A
        ),
        (# Case #2
            [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]
            ], # T
            1, # L
            [1,2] # A
        )
    )
    @unpack
    def test_answer(self, T, L, A):
        self.assertEquals(A, solution.answer(T, L))
    
