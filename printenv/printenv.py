import os
import sys

def wrap(char):
    if char == '\n':
        char = '\\n'
    return "`{}`".format(char)

if __name__ == "__main__":
    foo = os.environ.get("foo")
    if foo is None:
        print("foo no defined", file=sys.stderr)
        exit(1)
    output = " ".join(wrap(char) for char in foo)
    line = "| {} | {} |".format(os.environ.get("NAME"), output)
    print(line)
