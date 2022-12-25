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
does CPython.
