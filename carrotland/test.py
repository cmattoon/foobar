import solution
import unittest
from ddt import ddt, data, unpack


@ddt
class CarrotlandTestCase(unittest.TestCase):

    @data(
        ([[2, 3], [6, 9], [10, 160]], 289),
        ([[91207, 89566], [-88690, -83026], [67100, 47194]], 1730960165)
    )
    @unpack
    def test_solution(self, verticies, expected):
        self.assertEquals(expected, solution.answer(verticies))


if __name__ == '__main__':
    unittest.main()
