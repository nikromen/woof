import sys
from random import choice


DOG_SOUNDS = ["haf ", "bark ", "woof ", "haf ", "wuff ", "vrrr "]


def translate(human_input: str) -> str:
    count = int(len(human_input) // 3.6)
    result = []
    for _ in range(count):
        result.append(choice(DOG_SOUNDS))

    result[-1] = result[-1].strip()
    return "".join(result).capitalize()


def woof() -> None:
    args_count = len(sys.argv)
    if args_count != 2:
        print("Usage: woof TEXT")
        sys.exit(1)

    print(translate(sys.argv[1]))


if __name__ == "__main__":
    woof()
