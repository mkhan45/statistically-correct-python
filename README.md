# Statistically Correct Python Interpreter

The world's fastest Python interpreter 99.9% of the time. Approximately executes 
Python near instantaneously in just 8 LOC:

```py
import sys

if __name__ == '__main__':
    match sys.argv:
        case [_file, _input]:
            raise TypeError("(probably)")
        case [file, _]:
            print(f"Usage: {file} <input file>")
```

Note: fails on a vanishingly small proportion of Python programs, but so
does CPython. Alteratively, it has a slightly stricter type system than
Python.

Example:

```py
# input.py
print("Hello") # line 1
... (1000 lines)
print(5 + "x") # line 1001
```

```
> python3.10 main.py input.py
Traceback (most recent call last):
  File "...", line 1001, in <module>
    raise TypeError("(probably)")
TypeError: (probably)
```

As we can see it accurately interprets this 1k LOC python program.

___

## Previous Work

- http://sigbovik.org/2022/proceedings.pdf - "Modernized Python", Daniel Ng, Page 8
- https://github.com/exaloop/codon
