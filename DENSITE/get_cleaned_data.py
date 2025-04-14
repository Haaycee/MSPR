import csv
import os
from glob import glob

# Directory containing the input files
input_dir = os.path.dirname(__file__)  # Directory of the current script
output_file = os.path.join(input_dir, "DENSITE-combined.csv")

# Function to clean and combine the files
def clean_and_combine(input_dir, output_path):
    # Dynamically find all DENSITE-*.csv files in the input directory
    input_files = glob(os.path.join(input_dir, "DENSITE-*.csv"))

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        # Write the header row
        writer.writerow(["Code département", "Nom du département", "Population municipale", "Year"])

        for file_path in input_files:
            # Extract the year from the filename (e.g., "DENSITE-2012.csv" -> "2012")
            year = os.path.basename(file_path).split("-")[1].split(".")[0]

            with open(file_path, "r", encoding="utf-8") as infile:
                reader = csv.reader(infile)
                for i, row in enumerate(reader):
                    if i == 0:
                        # Skip the header row in each input file
                        continue
                    if len(row) >= 3:
                        # Remove spaces in the population column and add the year
                        row[2] = row[2].replace(" ", "")
                        row.append(year)
                        writer.writerow(row)

# Clean and combine the files
clean_and_combine(input_dir, output_file)
print(f"Combined file saved to: {output_file}")