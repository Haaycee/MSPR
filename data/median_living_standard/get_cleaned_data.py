import pandas as pd

# Chemins à adapter selon ta structure
NIVEAU_VIE_MEDIAN_2017_FILE = "/home/thibault/Desktop/MSPR/data/median_living_standard/median_living_standard_2017.xlsx"
NIVEAU_VIE_MEDIAN_2022_FILE = "/home/thibault/Desktop/MSPR/data/median_living_standard/median_living_standard_2022.xlsx"

HEADER_LINE_2017 = 0
HEADER_LINE_2022 = 0

def get_cleaned_data():
    # --- Lecture et traitement pour l'année 2017 ---
    df_2017 = pd.read_excel(NIVEAU_VIE_MEDIAN_2017_FILE, header=HEADER_LINE_2017)
    df_2017['Department'] = df_2017['Code'].astype(str).str.zfill(2)
    df_2017['Median_Living_Standard'] = df_2017['Niveau de vie annuel médian (euros)']
    result_2017 = df_2017[['Department', 'Median_Living_Standard']].copy()
    result_2017['Year'] = 2017

    # --- Lecture et traitement pour l'année 2022 ---
    df_2022 = pd.read_excel(NIVEAU_VIE_MEDIAN_2022_FILE, header=HEADER_LINE_2022)
    df_2022['Department'] = df_2022['Code'].astype(str).str.zfill(2)
    df_2022['Median_Living_Standard'] = df_2022['Niveau de vie annuel médian (euros)']
    result_2022 = df_2022[['Department', 'Median_Living_Standard']].copy()
    result_2022['Year'] = 2022

    dict_2017 = result_2017.set_index('Department')['Median_Living_Standard'].to_dict()
    dict_2022 = result_2022.set_index('Department')['Median_Living_Standard'].to_dict()

    return {
        "2017": dict_2017,
        "2022": dict_2022,
    }