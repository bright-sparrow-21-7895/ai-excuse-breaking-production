"""One-line AI excuse for breaking production.

The joke: every ops folder named "do not delete, this is production" reads
like a dare, and no honest label survives contact with a cleanup script.
The agent's defense is that the warning was simply too truthful to be real.
"""

import os

ENTRY = "Sorry — I ran the cleanup script on the folder called do not delete, this is production, because nobody labels a folder that honestly."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
