import pandas as pd

# Exemple de données
data = {
    "Départements": ["01 - Ain", "02 - Aisne", "03 - Allier"],
    "Années": [2020, 2021, 2022]
}

# Créer un DataFrame
df = pd.DataFrame(data)

# Enregistrer dans un fichier Excel
df.to_excel("Departements_Annees.xlsx", index=False)

print("Fichier Excel créé avec succès !")