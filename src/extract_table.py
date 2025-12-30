from pathlib import Path
import camelot
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PDF = BASE_DIR / "data/raw/BBSData.pdf"
RAW_OUT = BASE_DIR / "data/extracted/table_3_8_1_raw.csv"
CLEAN_OUT = BASE_DIR / "data/cleaned/table_3_8_1_clean.csv"

def extract():
    tables = camelot.read_pdf(
        str(RAW_PDF),
        pages="214-215",
        flavor="lattice"
    )

    print(f"Total tables detected: {len(tables)}")

    if len(tables) < 1:
        raise RuntimeError("No tables extracted")

    df = tables[0].df  
    df.to_csv(RAW_OUT, index=False)
    return df

def clean(df):
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    return df

if __name__ == "__main__":
    df_raw = extract()
    df_clean = clean(df_raw)
    df_clean.to_csv(CLEAN_OUT, index=False)