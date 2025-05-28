import pandas as pd

DENSITY_2017_FILE = "/home/thibault/Desktop/MSPR/data/density/density-2017.csv"
DENSITY_2022_FILE = "/home/thibault/Desktop/MSPR/data/density/density-2022.csv"

def get_cleaned_data():
    # Lecture des CSV
    df_2017 = pd.read_csv(DENSITY_2017_FILE)
    df_2022 = pd.read_csv(DENSITY_2022_FILE)

    # Normalisation du code département (toujours 2 caractères)
    df_2017['Department'] = df_2017['Code'].astype(str).str.zfill(2)
    df_2022['Department'] = df_2022['Code'].astype(str).str.zfill(2)

    # On veut la population municipale
    df_2017['Population'] = df_2017['Population municipale']
    df_2022['Population'] = df_2022['Population municipale']

    dict_2017 = df_2017.set_index('Department')['Population'].to_dict()
    dict_2022 = df_2022.set_index('Department')['Population'].to_dict()

    return {
        "2017": dict_2017,
        "2022": dict_2022,
    }

if __name__ == "__main__":
    print(get_cleaned_data())