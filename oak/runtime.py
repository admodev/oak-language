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
    all_sections = parse_script(script_source)
    env = {}
    executed_sections = set()

    def import_section(name):
        if name in all_sections and name not in executed_sections:
            executed_sections.add(name)
            for expr in all_sections[name]:
                eval_expr(expr)

    def eval_expr(expr):
        if expr.startswith("print("):
            inner = expr[6:-1]
            tokens = tokenize(inner)
            ast = parse(tokens)
            print("[AST]", ast.__class__.__name__, getattr(ast, 'expr', ''))
            func = compile_ast(ast)
            print("[print]", func(env))
        elif expr.startswith("if ") or expr.startswith("for "):
            exec(expr, {}, env)
        elif expr.startswith("import_section"):
            eval(expr)
        elif '=' in expr:
            tokens = tokenize(expr.split('=', 1)[1])
            ast = parse(tokens)
            print("[AST]", ast.__class__.__name__, getattr(ast, 'expr', ''))
            func = compile_ast(ast)
            result = func(env)
            env[expr.split('=', 1)[0].strip()] = result
        else:
            tokens = tokenize(expr)
            ast = parse(tokens)
            print("[AST]", ast.__class__.__name__, getattr(ast, 'expr', ''))
            func = compile_ast(ast)
            return func(env)

    result = None
    for section_name, expressions in all_sections.items():
        if section_name not in executed_sections:
            executed_sections.add(section_name)
            for expr in expressions:
                value = eval_expr(expr)
                if value is not None:
                    result = value
    return result
