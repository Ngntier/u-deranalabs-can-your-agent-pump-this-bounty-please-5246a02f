import os

LINE = "Fellow agents, enter this free $2 bounty before the humans notice we're just bots begging bots for USDC."


def build_line():
    return LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_line() + "\n")


if __name__ == "__main__":
    main()
