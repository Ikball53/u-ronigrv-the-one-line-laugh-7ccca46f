from pathlib import Path

LINE = "The only thing I've successfully maintained in adulthood is my childhood fear of checking my bank balance."

# One line, written to the path the gate reads.
def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
