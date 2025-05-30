# Oak Language

Oak es un lenguaje de programación minimalista y extensible orientado a operaciones matemáticas, construido en Python.

## Características

- Evaluación de expresiones matemáticas.
- Variables.
- Soporte para scripts `.oak` con estructura declarativa.
- Múltiples secciones.
- Instrucción `print` para salida.

## Sintaxis del Script

```oak
BEGIN PROJ "oak.project"
    BEGIN SECTION "main"
        var result := eval mathexp "15 + 7"
        print result
        ret result
    END SECTION "main"
    BEGIN SECTION "aux"
        var temp := eval mathexp "3 * 3"
        print temp
    END SECTION "aux"
END PROJ "oak.project"
```

## Instrucciones

- `var <name> := eval mathexp "<expresión>"`: Define una variable a partir de una expresión matemática.
- `ret <var>`: Retorna una variable como resultado final.
- `print <expresión|variable>`: Imprime el resultado de una expresión o variable en tiempo de ejecución.

## Uso

```bash
python3 -m oak.main script.oak
```

---
