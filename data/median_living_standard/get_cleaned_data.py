import pandas as pd

# À ajuster selon l'organisation de tes constantes ou chemins relatifs
NIVEAU_VIE_MEDIAN_2017_FILE = "/home/thibault/Desktop/MSPR/data/median_living_standard/Niveau_de_vie_median_2017.xlsx"
NIVEAU_VIE_MEDIAN_2022_FILE = "/home/thibault/Desktop/MSPR/data/median_living_standard/Niveau_de_vie_median_2017.xlsx"

HEADER_LINE_2017 = 0  # si le header commence à la première ligne, sinon ajuste
HEADER_LINE_2022 = 0  # pareil, ajuste si le fichier diffère

def get_cleaned_data():
    # --- Lecture et traitement pour l'année 2017 ---
    df_2017 = pd.read_excel(NIVEAU_VIE_MEDIAN_2017_FILE, header=HEADER_LINE_2017)
    print(df_2017.columns) # Pour vérifier les colonnes disponibles
    
    # Harmonisation des colonnes, adapte ici si besoin
    df_2017['Department'] = df_2017['Département'].astype(str).str.zfill(2)
    df_2017['Median_Living_Standard'] = df_2017['Valeur']
    
    result_2017 = df_2017[['Department', 'Median_Living_Standard']].copy()
    result_2017['Year'] = 2017

    # --- Lecture et traitement pour l'année 2022 ---
    df_2022 = pd.read_excel(NIVEAU_VIE_MEDIAN_2022_FILE, header=HEADER_LINE_2022)
    print(df_2022.columns) # Pour vérifier les colonnes disponibles
    df_2022['Department'] = df_2022['Department '].astype(str).str.zfill(2)
    df_2022['Median_Living_Standard'] = df_2022['Valeur']
    
    result_2022 = df_2022[['Department', 'Median_Living_Standard']].copy()
    result_2022['Year'] = 2022

    # Dictionnaires département => valeur
    dict_2017 = result_2017.set_index('Department')['Median_Living_Standard'].to_dict()
    dict_2022 = result_2022.set_index('Department')['Median_Living_Standard'].to_dict()

    # On retourne sous la même forme que l'immigration
    return {
        "2017": dict_2017,
        "2022": dict_2022,
    }