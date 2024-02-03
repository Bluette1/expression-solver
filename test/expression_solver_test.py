import unittest
from src import expression_solver as expression_solver

# evaluate_expression('(4-1)')
# evaluate_expression('(4 - 1) * (4 / (5 + 2) + 1)')
# evaluate_expression('12 * 3 / 12 + 3')
# evaluate_expression('(3 + 3) * 42 / (6 + 12)')
# evaluate_expression('1*(2+3+4)')
# evaluate_expression('3 + 12 * 3 / 12')
# evaluate_expression('3.3 + 12 * 3 / 12')


# Error Cases:
# evaluate_expression('4 (12E)')
# evaluate_expression('4 (41)')
# evaluate_expression('42+43**271')

class ExpressionSolverTest(unittest.TestCase):
    def test_basic(self):
      self.assertEqual(expression_solver.evaluate_expression('(4-1)'), 3, 'evaluate_expression(%s)' % ('4-1'))
    
    def test_with_brackets_different_operators(self):
      self.assertEqual(expression_solver.evaluate_expression('(4 - 1) * (4 / (5 + 2) + 1)'), 14, 'evaluate_expression(%s)' % ((4 - 1) * (4 / (5 + 2) + 1)))
  
    
if __name__ == '__main__':
  unittest.main()