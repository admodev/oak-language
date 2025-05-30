import re

def tokenize(source):
    tokens = []
    token = ''
    in_string = False

    for char in source:
        if char == '"':
            token += char
            if in_string:
                tokens.append(token)
                token = ''
                in_string = False
            else:
                if token.strip():
                    tokens.append(token.strip())
                token = '"'
                in_string = True
        elif in_string:
            token += char
        elif char.isspace():
            if token:
                tokens.append(token)
                token = ''
        elif char in '+-*/()=':
            if token:
                tokens.append(token)
            tokens.append(char)
            token = ''
        else:
            token += char

    if token:
        tokens.append(token)

    return tokens
