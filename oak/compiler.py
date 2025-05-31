# Casteo explicito de dill como pickle para no cambiar tanto codigo...
import dill as pickle

from .parser import Number, Var, BinOp, Assign, EvalMathExp, String, FunctionCall, Return, parse
from .tokenizer import tokenize

def compile_ast(node):
    if isinstance(node, Number):
        return lambda env: node.value

    if isinstance(node, Var):
        return lambda env: env.get(node.name, 0)

    if isinstance(node, Return):
        expr_fn = compile_ast(node.expr)
        def return_fn(env):
            val = expr_fn(env)
            env["_return"] = val
            return val
        return return_fn

    if isinstance(node, BinOp):
        left_fn = compile_ast(node.left)
        right_fn = compile_ast(node.right)
        op = node.op

        def eval_binop(env):
            l = left_fn(env)
            r = right_fn(env)
            if op == '+':
                return l + r
            elif op == '-':
                return l - r
            elif op == '*':
                return l * r
            elif op == '/':
                return l / r
            else:
                raise ValueError(f"Unknown operator {op}")
        return eval_binop

    if isinstance(node, Assign):
        expr_fn = compile_ast(node.expr)
        def assign_fn(env):
            val = expr_fn(env)
            env[node.name] = val
            return val
        return assign_fn

    if isinstance(node, EvalMathExp):
        expr = node.expr
        def eval_math_fn(env):
            try:
                # Validar caracteres para seguridad: solo dígitos, operadores, espacios, paréntesis y punto decimal
                allowed_chars = "0123456789.+-*/ ()"
                if any(c not in allowed_chars for c in expr):
                    raise ValueError(f"Expresión no permitida para evaluar: {expr}")
                # Evalua la expresión sin acceso a builtins ni variables externas
                return eval(expr, {"__builtins__": None}, {})
            except Exception as e:
                raise ValueError(f"Error evaluando expresión matemática: {expr}") from e
        return eval_math_fn
    
    if isinstance(node, String):
        return lambda env: node.value
    
    if isinstance(node, FunctionCall):
        if node.name == "print":
            arg_fns = [compile_ast(arg) for arg in node.args]
            def print_fn(env):
                values = [arg(env) for arg in arg_fns]
                print(*values)
                return values[0] if values else None
            return print_fn

    raise ValueError(f"Tipo de nodo desconocido: {type(node)}")

def compile_script(all_sections):
    compiled_sections = {}
    compiled_expressions = []
    
    compiled_expressions.append("; binary compilation made with Oak Compiler. 2025")
    compiled_expressions.append("section")
    compiled_expressions.append(".text")
    compiled_expressions.append("global")
    compiled_expressions.append("_start")
    
    for section_name, expressions in all_sections.items():
        for i, expr in enumerate(expressions):
            tokens = tokenize(expr)
            ast = parse(tokens)
            fn = compile_ast(ast)
            
            print(f"[DEBUG] tokens: {tokens}")
            
            # Handle all token cases and translating them to assembly code
            if tokens[i] == "print":
                print(f"[COMPILING] print definition found, translating...")
                compiled_expressions.append("mov eax, 3")
    for comp_exp in compiled_expressions:
      print(f"[DEBUG] {comp_exp}")
    return compiled_sections

def save_binary_script(compiled, output_path):
    with open(output_path, "wb") as f:
        pickle.dump(compiled, f)
