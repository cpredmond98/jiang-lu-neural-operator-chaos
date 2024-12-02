from neural_chaos import hello
from pathlib import Path


BASE_DIR = Path(".").parent.parent


def main() -> None:
    print("Hello from jiang-lu-neural-operator-chaos!")
    print(hello())
