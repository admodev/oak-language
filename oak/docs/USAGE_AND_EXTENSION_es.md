# Oak Language

Oak es un lenguaje de programación minimalista y extensible orientado a operaciones matemáticas, construido en Python.

## Características

- Evaluación de expresiones matemáticas.
- Variables.
- Soporte para scripts `.oak` con estructura declarativa.
- Múltiples secciones.
- Instrucciones `print`, `if`, `loop`, `import`.

## Sintaxis del Script

```oak
BEGIN PROJ "oak.project"
    BEGIN SECTION "math"
        var x := eval mathexp "10 * 3"
        print x
    END SECTION "math"

    BEGIN SECTION "main"
        import math
        loop 2
            print x
        ret x
    END SECTION "main"
END PROJ "oak.project"
```

## Instrucciones

- `var <name> := eval mathexp "<expresión>"`: Define una variable.
- `ret <var>`: Retorna una variable.
- `print <expresión>`: Imprime una expresión.
- `if <condición>`: Condición booleana (sintaxis Python válida).
- `loop <n>`: Ejecuta un bloque n veces.
- `import <sección>`: Ejecuta otra sección antes de continuar.

## Uso

```bash
python3 -m oak.main script.oak
```

---
