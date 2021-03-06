import os
import subprocess
import sys

if __name__ == "__main__":
    input_ = os.environb.get(b"INPUT")
    if input_ is None:
        print("[write_env] INPUT undefined", file=sys.stderr)
        exit(1)

    with open(".env", "wb") as dotenv_file:
        dotenv_file.write(input_)

    result = subprocess.run(sys.argv[1:], check=False)
    sys.exit(result.returncode)
