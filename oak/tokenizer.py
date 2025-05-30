def tokenize(source):
    tokens = []
    current = ''
    i = 0
    while i < len(source):
        char = source[i]
        
        # Manejo del token :=
        if char == ':' and i + 1 < len(source) and source[i + 1] == '=':
            if current:
                tokens.append(current)
                current = ''
            tokens.append(':=')
            i += 2
            continue
        
        if char.isspace():
            if current:
                tokens.append(current)
                current = ''
        elif char in '+-*/=()':
            if current:
                tokens.append(current)
                current = ''
            tokens.append(char)
        elif char == '"':
            if current:
                tokens.append(current)
                current = '"'
        elif char.isalnum() or char == '.' or char == '_':
            current += char
        else:
            raise ValueError(f"Unexpected character: {char}")
        i += 1
    
    if current:
        tokens.append(current)
    return tokens
