import os
import sys

if __name__ == "__main__":
    foo = os.environb.get(b"foo")
    if foo is None:
        print("[print_env] foo undefined", file=sys.stderr)
        exit(1)

    sys.stdout.buffer.write(foo)
