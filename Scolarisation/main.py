import os
import pandas as pd
from pathlib import Path

# List of all French departments (metropolitan and overseas)
FRENCH_DEPARTMENTS = [
    # Metropolitan France
    "Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", 
    "Alpes-Maritimes", "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", 
    "Bouches-du-Rhône", "Calvados", "Cantal", "Charente", "Charente-Maritime", "Cher",
    "Corrèze", "Corse-du-Sud", "Haute-Corse", "Côte-d'Or", "Côtes-d'Armor", "Creuse",
    "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", 
    "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", 
    "Indre-et-Loire", "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire",
    "Loire-Atlantique", "Loiret", "Lot", "Lot-et-Garonne", "Lozère", "Maine-et-Loire",
    "Manche", "Marne", "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", "Meuse", "Morbihan",
    "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", 
    "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", 
    "Haut-Rhin", "Rhône", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", 
    "Haute-Savoie", "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", 
    "Somme", "Tarn", "Tarn-et-Garonne", "Var", "Vaucluse", "Vendée", "Vienne", 
    "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", "Essonne", 
    "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise",
    # Overseas departments
    "Guadeloupe", "Martinique", "Guyane", "La Réunion", "Mayotte"
]

# Academic regions
ACADEMIC_REGIONS = [
    "Aix-Marseille", "Amiens", "Besançon", "Bordeaux", "Caen", "Clermont-Ferrand", 
    "Corse", "Créteil", "Dijon", "Grenoble", "Lille", "Limoges", "Lyon", "Montpellier", 
    "Nancy-Metz", "Nantes", "Nice", "Orléans-Tours", "Paris", "Poitiers", "Reims", 
    "Rennes", "Rouen", "Strasbourg", "Toulouse", "Versailles"
]

def read_csv_files(input_dir='data/input'):
    """
    Read all CSV files from the specified input directory
    
    Args:
        input_dir (str): Path to the directory containing CSV files
    
    Returns:
        dict: Dictionary with filenames as keys and pandas DataFrames as values
    """
    # Create the input directory path
    input_path = Path(input_dir)
    
    # Check if directory exists
    if not input_path.exists():
        print(f"Error: Directory '{input_dir}' does not exist")
        return {}
    
    # Dictionary to store dataframes
    dataframes = {}
    
    # List all files in the directory
    for file in os.listdir(input_path):
        # Check if the file is a CSV file
        if file.lower().endswith('.csv'):
            file_path = input_path / file
            try:
                # Read the CSV file into a pandas DataFrame
                df = pd.read_csv(file_path)
                dataframes[file] = df
                print(f"Successfully read '{file}' with {len(df)} rows and {len(df.columns)} columns")
                print(f"Columns: {', '.join(df.columns)}")

                # keep only lines with the department name in the 'Tables Départements et académies' column
                df = df[df['Tables Départements et académies'].isin(FRENCH_DEPARTMENTS)]

                # Keep only columns : "Tables Départements et académies","Tables Effectifs scolarisés (1)","Tables Effectifs d’habitants","Tables Taux de scolari- sation (%)" and rename thems
                df = df[["Tables Départements et académies","Tables Effectifs scolarisés (1)","Tables Effectifs d’habitants","Tables Taux de scolari- sation (%)"]]
                df = df.rename(columns={"Tables Départements et académies":"Departement","Tables Effectifs scolarisés (1)":"Effectifs scolarisés","Tables Effectifs d’habitants":"Effectifs habitants","Tables Taux de scolari- sation (%)":"Taux de scolarisation"})

                # Save the new dataframe in a new csv file
                df.to_csv(f"data/output/{file}", index=False)
                print(f"Successfully saved '{file}' with {len(df)} rows and {len(df.columns)} columns")

            except Exception as e:
                print(f"Error reading '{file}': {str(e)}")
    
    if not dataframes:
        print(f"No CSV files found in '{input_dir}'")
    else:
        print(f"Total CSV files read: {len(dataframes)}")
    
    return dataframes

if __name__ == "__main__":
    # Read all CSV files from the data/input directory
    csv_data = read_csv_files()
    
    # You can access individual dataframes like this:
    # If there's a file named example.csv in the input directory:
    # example_df = csv_data.get('example.csv')
    
    # Print the names of all loaded files
    print("\nLoaded CSV files:")
    for filename in csv_data.keys():
        print(f"- {filename}")