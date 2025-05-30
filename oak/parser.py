class Node:
    pass

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number(Node):
    def __init__(self, value):
        self.value = float(value)

class Var(Node):
    def __init__(self, name):
        self.name = name

class Assign(Node):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

def parse(tokens):
    def parse_expr(index):
        left, index = parse_term(index)
        while index < len(tokens) and tokens[index] in ('+', '-'):
            op = tokens[index]
            right, index = parse_term(index + 1)
            left = BinOp(left, op, right)
        return left, index

    def parse_term(index):
        left, index = parse_factor(index)
        while index < len(tokens) and tokens[index] in ('*', '/'):
            op = tokens[index]
            right, index = parse_factor(index + 1)
            left = BinOp(left, op, right)
        return left, index

    def parse_factor(index):
        token = tokens[index]
        if token == '(':
            expr, index = parse_expr(index + 1)
            if tokens[index] != ')':
                raise ValueError("Expected )")
            return expr, index + 1
        elif token.replace('.', '', 1).isdigit():
            return Number(token), index + 1
        elif token.isalpha():
            if index + 1 < len(tokens) and tokens[index + 1] == '=':
                expr, new_index = parse_expr(index + 2)
                return Assign(token, expr), new_index
            return Var(token), index + 1
        else:
            raise ValueError(f"Unexpected token: {token}")

    tree, _ = parse_expr(0)
    return tree

