import unittest
from src import expression_solver as expression_solver


class ExpressionSolverTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '(4-1)'), 3, 'evaluate_expression(%s)' % ('4-1'))

    def test_with_brackets_different_operators_decimals(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '(4 - 1) * (4 / (5 + 2) + 1)'), 4.71, 'evaluate_expression(%s)' % ('(4 - 1) * (4 / (5 + 2) + 1)'))

    def test_with_no_brackets(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '3 + 12 * 3 / 12'), 6, 'evaluate_expression(%s)' % ('3 + 12 * 3 / 12'))

    def test_with_brackets_different_operators(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '(3 + 3) * 42 / (6 + 12)'), 14, 'evaluate_expression(%s)' % ('(3 + 3) * 42 / (6 + 12)'))

    def test_with_no_spaces_in_expression(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '1*(2+3+4)'), 9, 'evaluate_expression(%s)' % ('1*(2+3+4)'))

    def test_with_no_brackets_other_way_round(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '12 * 3 / 12 + 3'), 6, 'evaluate_expression(%s)' % ('12 * 3 / 12 + 3'))

    def test_with_no_brackets_decimals(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '3.3 + 12 * 3 / 12'), 6.3, 'evaluate_expression(%s)' % ('3.3 + 12 * 3 / 12'))

    # Error Cases:

    def test_invalid_operator(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '4 (12E)'), 'Invalid Expression', 'evaluate_expression(%s)' % ('4 (12E)'))

    def test_invalid_operator_other(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '42+43**271'), 'Invalid Expression', 'evaluate_expression(%s)' % ('42+43**271'))

    def test_no_valid_operator(self):
        self.assertEqual(expression_solver.evaluate_expression(
            '4 (41)'), 'Invalid Expression', 'evaluate_expression(%s)' % ('4 (41)'))


if __name__ == '__main__':
    unittest.main()
