'''
To solve algebraic expressions, we'll take the following steps
  1.Convert the infix algebraic expression into a postfix expression
  2.Solve the postfix expression using either
    a) a stack
    b) expression tree
'''


def evaluate_tree(root):
    if (root.value.isnumeric()):
        return root.value
    left_side = evaluate_tree(root.left_child)
    right_side = evaluate_tree(root.right_child)

    return int(evaluate([left_side, right_side], root.value))


def print_tree(root, str=[]):  # Inorder traversal gives infix expression
    if (root != None):
        if root.left_child:
            str = str + print_tree(root.left_child, [])
        str += [root.value]
        if root.right_child:
            str = str + print_tree(root.right_child, [])

    return str


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def build_expression_tree(expression):
    expression = expression.split(' ')

    stack = []
    for idx in range(len(expression)):
        if (expression[idx]).isnumeric():  # is an operand
            new_node = Node(expression[idx])
            stack.append(new_node)
        else:  # is an operator
            new_node = Node(expression[idx])
            new_node.right_child = stack.pop()

            new_node.left_child = stack.pop()
            stack.append(new_node)

    return stack[0]  # root of expression tree


def convert_to_postfix(expression):
    expression = ''.join(expression.split(' '))

    precedence_map = {
        "/": 2,
        '*': 2,
        '+': 1,
        '-': 1
    }
    postfix = []
    stack = []
    next = 0
    for idx in range(len(expression)):
        if (next > idx):
            continue
        if ((expression[idx]).isnumeric()):  # is an operand
            next = idx + 1
            while(next < len(expression) and (expression[next]).isnumeric()):
                next = next + 1
            postfix.append(expression[idx:next])  # add it to postfix
        else:
            current = expression[idx]
            if(len(stack) == 0):
                stack.append(current)
            elif current == ')':
                while len(stack) != 0 and stack[-1] != '(':
                    operator = stack.pop()
                    postfix.append(operator)
                stack.pop()
            elif(current == '(' or stack[-1] == '('):
                stack.append(current)
            else:
                while len(stack) != 0 and stack[-1] != '(' and precedence_map[current] <= precedence_map[stack[-1]]:
                    operator = stack.pop()
                    postfix.append(operator)
                stack.append(current)

    while len(stack) != 0:
        postfix.append(stack.pop())

    return postfix


# postfix = convert_to_postfix('(4-1)')
postfix = convert_to_postfix('(4 - 1) * (4 / (5 + 2) + 1)')
# postfix = convert_to_postfix('12 * 3 / 12 + 3')
# postfix = convert_to_postfix('(3 + 3) * 42 / (6 + 12)')
# TREE 12 + 6 / 42 * 3 + 3
# TREE (12 + 6) / 42 *(3 + 3)
# TREE 3 + 3 * 42 / 6 + 12

# postfix = convert_to_postfix('1*(2+3+4)')
postfix = convert_to_postfix('3 + 12 * 3 / 12')

print('Postfix: ', postfix)


def evaluate(operands, operator):

    if operator == '/':
        return int(operands[0]) / int(operands[1])

    elif operator == '*':
        return int(operands[0]) * int(operands[1])

    elif operator == '+':
        return int(operands[0]) + int(operands[1])

    elif operator == '-':
        return int(operands[0]) - int(operands[1])


def solve_expression(expression):
    expression = expression.split(' ')
    stack = []
    for idx in range(len(expression)):
        if ((expression[idx]).isnumeric()):
            stack.append(expression[idx])
        else:
            operator = expression[idx]
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            solution = evaluate([operand_1, operand_2], operator)
            stack.append(solution)
    return int(stack[0])


# solved = solve_expression('4 1 - 4 5 2 + / 1 + *')

# solved = solve_expression('3 12 + * 3 12 /')

# solved = solve_expression('2 4 + 4 6 + *')

# solved = solve_expression('3 3 + 42 * 6 12 + /')
solved = solve_expression(' '.join(postfix))

print('SOLUTION STACK: ', solved)

expression_tree_root = build_expression_tree(' '.join(postfix))

# print('TREE: ', ' '.join(print_tree(expression_tree_root, [])))
print('SOLUTION TREE: ', evaluate_tree(expression_tree_root))
