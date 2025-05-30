def tokenize(source):
    tokens = []
    current = ''
    for char in source:
        if char.isspace():
            continue
        elif char in '+-*/=()':
            if current:
                tokens.append(current)
                current = ''
            tokens.append(char)
        elif char.isdigit() or char.isalpha() or char == '.':
            current += char
        else:
            raise ValueError(f"Unexpected character: {char}")
    if current:
        tokens.append(current)
    return tokens

