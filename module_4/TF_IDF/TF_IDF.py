import sys
import re


def emit(tupl: tuple, value: int = 1) -> None:
    word, docname = tupl
    print(f"{word}#{docname}\t{value}")


def _map(docname: str, content: list) -> None:
    for word in content:
        word = word.strip()
        if word:
            emit((word, docname), 1)


def main() -> None:
    for line in sys.stdin:
        docname, value = line.rstrip().split(":", 1)
        value = re.sub(r"[\W_]", " ", value)
        _map(docname, value.split(" "))


if __name__ == '__main__':
    main()
