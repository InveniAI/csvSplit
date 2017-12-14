import pandas as pd
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

merged = []

print files

for f in files:

    filename, ext = os.path.splitext(f)

    if ext == '.csv':

        read = pd.read_csv(f)
        merged.append(read)

result = pd.concat(merged)
result.to_csv('Oncology.csv')
