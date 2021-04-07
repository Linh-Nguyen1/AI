import pandas as pd
import os


# Concatenate the DataFrames and save as corpus

# Get csv file names in output directory
path = os.getcwd() + "/stimulus/"
files = os.listdir(path)

# Create a list to store DataFrames
df_list = []

# Iterate over files in output dir and append DataFrames into df_list
for file in files:
    df = pd.read_csv(path + file, index_col=None)
    df_list.append(df)

# Create a DataFrame
stimulus_raw = pd.concat(df_list, axis=0, ignore_index=True)

# Save the DataFrame as a csv file
stimulus_raw.to_csv("stimulus_raw.csv")
