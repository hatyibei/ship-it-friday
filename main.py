"""Entry for Ship It Friday: writes the reckless Friday commit message to /output/entry.txt."""

import os

TEXT = "fix: tiny untested change, skipping review because it's friday at 4:59 pm and I have never once been wrong about a deploy"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
