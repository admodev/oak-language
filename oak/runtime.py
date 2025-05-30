from .tokenizer import tokenize
from .parser import parse
from .compiler import compile_ast
from .script_parser import parse_script

def run(source):
    tokens = tokenize(source)
    ast = parse(tokens)
    env = {}
    func = compile_ast(ast)
    result = func(env)
    return result

def run_script(script_source):
    sections = parse_script(script_source)
    env = {}
    result = None
    for section_name, expressions in sections.items():
        for expr in expressions:
            if expr.startswith("print("):
                expr_inner = expr[6:-1]  # lo que va dentro del print()
                tokens = tokenize(expr_inner)
                ast = parse(tokens)
                func = compile_ast(ast)
                print("[print]", func(env))
            else:
                tokens = tokenize(expr)
                ast = parse(tokens)
                func = compile_ast(ast)
                result = func(env)
    return result
