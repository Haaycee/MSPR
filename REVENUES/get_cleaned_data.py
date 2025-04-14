import pandas as pd
import os

# Liste des fichiers CSV à combiner
csv_files = [
    "/home/thibault/REPO MSPR/MSPR/REVENUES/revenus_2012.csv",
    "/home/thibault/REPO MSPR/MSPR/REVENUES/revenus_2017.csv",
    "/home/thibault/REPO MSPR/MSPR/REVENUES/revenus_2022.csv"
]

# Vérifier si tous les fichiers existent
for file in csv_files:
    if not os.path.exists(file):
        print(f"Erreur : Le fichier {file} est introuvable.")
        exit(1)

# Lire et combiner les fichiers CSV
dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combiner tous les DataFrames en un seul
combined_df = pd.concat(dataframes, ignore_index=True)

# Sauvegarder le fichier combiné
output_file = "/home/thibault/REPO MSPR/MSPR/REVENUES/revenus_combines.csv"
combined_df.to_csv(output_file, index=False)

print(f"Les fichiers ont été combinés avec succès dans {output_file}.")