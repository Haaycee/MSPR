import pandas as pd

NATALITY_RATE_FILE = "/home/thibault/Desktop/MSPR/data/natality/insee_rp_evol_1968.xlsx"  # adapte le chemin

def get_cleaned_data():
    df = pd.read_excel(NATALITY_RATE_FILE, header=4, dtype={"codgeo": str})
    keep_periods = ["2010-2015", "2015-2021"]
    df = df[df["an"].isin(keep_periods)]
    df["codgeo"] = df["codgeo"].astype(str).str.zfill(2)
    result = {}
    # Remapping
    period_to_year = {
        "2010-2015": "2017",
        "2015-2021": "2022"
    }
    for period, year in period_to_year.items():
        sub = df[df["an"] == period]
        result[year] = sub.set_index("codgeo")["tx_nat"].astype(float).to_dict()
    return result

if __name__ == "__main__":
    print(get_cleaned_data())