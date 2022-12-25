import sys

if __name__ == '__main__':
    match sys.argv:
        case [_file, _input]:
            raise TypeError("(probably)")
        case [file, _]:
            print(f"Usage: {file} <input file>")
