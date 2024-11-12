import pandas as pd
import os

# Print all files in the directory
directory = '/Users/manuel/Documents/GitHub/JeanPierreWeill/Data /MetaOrgarnic /GoogleSheets'
print("Files in directory:")
for file in os.listdir(directory):
    print(file)

