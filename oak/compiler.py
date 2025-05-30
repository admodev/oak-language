from .parser import Number, BinOp, Var, Assign

def compile_ast(ast):
    if isinstance(ast, Number):
        return lambda env: ast.value
    elif isinstance(ast, Var):
        return lambda env: env.get(ast.name, 0)
    elif isinstance(ast, BinOp):
        left = compile_ast(ast.left)
        right = compile_ast(ast.right)
        return lambda env: eval(f"{left(env)} {ast.op} {right(env)}")
    elif isinstance(ast, Assign):
        expr = compile_ast(ast.expr)
        return lambda env: env.update({ast.name: expr(env)}) or env[ast.name]
    else:
        raise ValueError("Unknown AST node")

