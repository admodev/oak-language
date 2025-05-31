import re

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

def run_script_in_debug_mode(script_source):
    print("RUNNING IN DEBUG MODE!")
    
    all_sections = parse_script(script_source)
    env = {}
    executed_sections = set()

    def import_section(name):
        if name in all_sections and name not in executed_sections:
            executed_sections.add(name)
            for expr in all_sections[name]:
                eval_expr(expr)

    def eval_expr(expr):
        expr = expr.strip()
        match = re.match(r'print\s+(?:"([^"]+)"|\'([^\']+)\')', expr)
        
        if match:
            text = match.group(1) if match.group(1) is not None else match.group(2)
            print("[print]", text)
            return text
        if expr.startswith("print "):
            match = re.match(r'print\s+"(.+?)"|print\s+\'(.+?)\'', expr)
            if match:
                text = match.group(1) or match.group(2)
                print("[print]", text)
                return text
        if expr.startswith("print("):
            inner = expr[6:-1]
            tokens = tokenize(inner)
            ast_node = parse(tokens)
            func = compile_ast(ast_node)
            result = func(env)
            print("[print]", result)
            return result
        elif expr.startswith("if ") or expr.startswith("for "):
            exec(expr, {}, env)
        elif expr.startswith("import_section"):
            eval(expr)
        elif '=' in expr:
            lhs, rhs = expr.split('=', 1)
            tokens = tokenize(rhs)
            ast = parse(tokens)
            func = compile_ast(ast)
            result = func(env)
            env[lhs.strip()] = result
            return result
        else:
            tokens = tokenize(expr)
            ast = parse(tokens)
            func = compile_ast(ast)
            return func(env)

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
        expr = expr.strip()
        match = re.match(r'print\s+(?:"([^"]+)"|\'([^\']+)\')', expr)
        
        if match:
            text = match.group(1) if match.group(1) is not None else match.group(2)
            print("[print]", text)
            return text
        if expr.startswith("print "):
            match = re.match(r'print\s+"(.+?)"|print\s+\'(.+?)\'', expr)
            if match:
                text = match.group(1) or match.group(2)
                print("[print]", text)
                return text
        if expr.startswith("print("):
            inner = expr[6:-1]
            tokens = tokenize(inner)
            ast_node = parse(tokens)
            func = compile_ast(ast_node)
            result = func(env)
            print("[print]", result)
            return result
        elif expr.startswith("if ") or expr.startswith("for "):
            exec(expr, {}, env)
        elif expr.startswith("import_section"):
            eval(expr)
        elif '=' in expr:
            lhs, rhs = expr.split('=', 1)
            tokens = tokenize(rhs)
            ast = parse(tokens)
            func = compile_ast(ast)
            result = func(env)
            env[lhs.strip()] = result
            return result
        else:
            tokens = tokenize(expr)
            ast = parse(tokens)
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
