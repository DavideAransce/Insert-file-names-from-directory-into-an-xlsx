import os
import pandas as pd

# Specify the directory containing your files
DIRPATH = input('Insert whole directory path starting from C:')

directory =  r"DIRPATH"

# Get a list of file names
files = os.listdir(directory)

# Create a DataFrame from the file names
df = pd.DataFrame(files, columns=['File_Name'])

# Write the DataFrame to an Excel file
output_path = 'file_names.xlsx'
df.to_excel(output_path, index=False)

print(f'File names have been saved to {output_path}')
