import re

def parse_script(source):
    """
    Parsea un script .oak y devuelve una lista de expresiones a evaluar por sección.
    """
    lines = source.strip().splitlines()
    in_section = None
    sections = {}

    for line in lines:
        line = line.strip()
        if line.startswith("BEGIN SECTION"):
            section_name = re.findall(r'"(.*?)"', line)[0]
            in_section = section_name
            sections[in_section] = []
        elif line.startswith("END SECTION"):
            in_section = None
        elif in_section:
            if line.startswith("var "):
                match = re.match(r'var (\w+) := eval mathexp \"([^\"]+)\"', line)
                if match:
                    var_name = match.group(1)
                    expr = match.group(2)
                    sections[in_section].append(f'{var_name} = {expr}')
            elif line.startswith("ret "):
                var_name = line[4:].strip()
                sections[in_section].append(var_name)
            elif line.startswith("print "):
                expr = line[6:].strip()
                sections[in_section].append(f'print({expr})')
    return sections
