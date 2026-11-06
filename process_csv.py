from pathlib import Path

import pandas as pd


INPUT_FILE = Path(__file__).with_name("RW_WW_ohne_leere_Werte.csv")
OUTPUT_DIR = Path(__file__).with_name("summaries")
CHUNK_SIZE = 100_000
SUM_COLUMNS = ["RW", "WW", "RW_WW"]


def main() -> None:
    row_count = 0
    totals = pd.DataFrame(columns=SUM_COLUMNS, dtype="float64")

    # Read a portion at a time so the full CSV does not need to fit in memory.
    for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE):
        row_count += len(chunk)

        # Calculate this chunk's sums for each Name, then add them to prior chunks.
        chunk_totals = chunk.groupby("Name")[SUM_COLUMNS].sum()
        totals = totals.add(chunk_totals, fill_value=0)

    # Save one summary row and CSV file for each Name found in the input.
    OUTPUT_DIR.mkdir(exist_ok=True)
    for name, values in totals.iterrows():
        summary = values.to_frame().T
        summary.insert(0, "Name", name)
        output_file = OUTPUT_DIR / f"{name}_summary.csv"
        # The UTF-8 BOM helps Excel display names with accented characters correctly.
        summary.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"Saved {output_file.name}")

    print(f"\nProcessed {row_count:,} rows from {INPUT_FILE.name}")
    print("Totals by Name:")
    print(totals.to_string())


if __name__ == "__main__":
    main()