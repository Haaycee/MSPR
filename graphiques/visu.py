import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("../dataset.xlsx")  # adapte le chemin si besoin

# Génère dynamiquement la liste des critères : toutes les colonnes numériques, sauf celles qui concernent les votes
votes = [
    "vote_pct_Renaissance", "vote_pct_LR", "vote_pct_RN", "vote_pct_LO",
    "vote_pct_DLF", "vote_pct_Résistons", "vote_pct_Génération.s", "vote_pct_UPR",
    "vote_pct_LFI", "vote_pct_SP", "vote_pct_NPA"
]

# Critères = toutes les numériques sauf les votes (et éventuellement sauf l'id ou code_departement)
criteres = [
    col for col in df.select_dtypes(include="number").columns
    if col not in votes and not col.startswith('vote_')
    and "code" not in col.lower() and "id" not in col.lower()
]

# Nettoyage éventuel
for col in criteres + votes:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace('\u202f', '', regex=False)
            .str.replace(' ', '', regex=False)
            .replace('', '0')
            .astype(float)
        )

# Matrice critères (lignes) x votes (colonnes) SANS vote sur l'axe vertical
corr_matrix = df[criteres + votes].corr().loc[criteres, votes]

plt.figure(figsize=(14, max(8, len(criteres) * 0.5)))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1, vmax=1
)
plt.title("Corrélation entre critères et résultats de votes")
plt.ylabel("Critères")
plt.xlabel("Votes")
plt.tight_layout()
plt.show()

print("Critères utilisés (axe Y):", criteres)
print("Votes utilisés (axe X):", votes)