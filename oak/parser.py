class Node:
    pass

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class EvalMathExp(Node):
  def __init__(self, expr_tokens):
    self.expr = ' '.join(expr_tokens)

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

class String(Node):
    def __init__(self, value):
        self.value = value

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

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
        elif token.startswith('"') and token.endswith('"'):
            return String(token[1:-1]), index + 1
        elif token == "eval" and index + 1 < len(tokens) and tokens[index + 1] == "mathexp":
            expr_tokens = tokens[index + 2:]
            expr_str = ' '.join(expr_tokens)
            return EvalMathExp(expr_str), len(tokens)
        elif token.isalpha():
            if index + 1 < len(tokens) and tokens[index + 1] == '(':
                # funciones con un argumento
                arg, new_index = parse_expr(index + 2)
                if tokens[new_index] != ')':
                    raise ValueError("Expected ) after function argument")
                return FunctionCall(token, [arg]), new_index + 1
            if index + 1 < len(tokens) and tokens[index + 1] == '=':
                expr, new_index = parse_expr(index + 2)
                return Assign(token, expr), new_index
            return Var(token), index + 1
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_statement(index):
        if tokens[index] == 'var':
            # var result := ...
            var_name = tokens[index + 1]
            if tokens[index + 2] != ':=':
                raise ValueError("Expected ':=' after var <name>")
            if tokens[index + 3] == 'eval' and tokens[index + 4] == 'mathexp':
                expr_tokens = tokens[index + 5:]
                return Assign(var_name, EvalMathExp(expr_tokens)), len(tokens)
            else:
                expr, new_index = parse_expr(index + 3)
                return Assign(var_name, expr), new_index
        elif tokens[index] == 'ret':
            expr, new_index = parse_expr(index + 1)
            return Return(expr), new_index
        else:
            # Por defecto, parsea una expresión normal
            return parse_expr(index)

    tree, _ = parse_statement(0)
    return tree
