from unittest import TestCase
from matrix_addition import add_matrices
from unittest.mock import patch
import io

"""
 a) two square matrices that are 1x1
 b) two square matrices that are 2x2
 c) two square matrices that are 3x3
 d) two rectangular matrices that are 3x4 or 4x3
 e) two homogenous matrices (matrices whose elements are all the same value)
 f) two matrices of size 1x4 or 4x1 (vectors, some would call them!)
 g) one exceptional situation.
"""


class Test(TestCase):
    def test_first_1_1_second_1_1_(self):
        first_matrix = [[1]]
        second_matrix = [[2]]
        expected = [[3]]
        self.assertEqual(expected, add_matrices(first_matrix, second_matrix))

    def test_first_2_2_second_2_2_(self):
        first_matrix = [[1, 1], [2, 2]]
        second_matrix = [[0, 1], [1, 0]]
        expected = [[1, 2], [3, 2]]
        self.assertEqual(expected, add_matrices(first_matrix, second_matrix))

    def test_first_3_3_second_3_3_(self):
        first_matrix = [[1, 1, 0], [2, 2, 0], [1, 1, 1]]
        second_matrix = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
        expected = [[1, 2, 0], [3, 2, 0], [2, 2, 2]]
        self.assertEqual(expected, add_matrices(first_matrix, second_matrix))

    def test_first_3_4_second_3_4_(self):
        first_matrix = [[1, 1, 0], [2, 2, 0], [1, 1, 1], [2, 2, 4]]
        second_matrix = [[0, 1, 0], [1, 0, 0], [1, 1, 1], [1, 1, 1]]
        expected = [[1, 2, 0], [3, 2, 0], [2, 2, 2], [3, 3, 5]]
        self.assertEqual(expected, add_matrices(first_matrix, second_matrix))

    def test_first_3_3_second_3_3_homogeneous(self):
        first_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        second_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected = [[2, 4, 6], [2, 4, 6], [2, 4, 6]]
        self.assertEqual(expected, add_matrices(first_matrix, second_matrix))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exception(self, mock_output):
        first_matrix = [[1, 2, 3], [1, 2, 3]]
        second_matrix = [[1, 2], [1, 2]]
        add_matrices(first_matrix, second_matrix)
        printed = mock_output.getvalue()
        expected = "Different size of matrices. Cannot calculate sum!\n"
        self.assertEqual(expected, printed)