# Packages
import os
import pandas as pd
import zipfile
from lib.logging import *

# Extract
with zipfile.ZipFile('data/the-car-connection-picture-dataset.zip', 'r') as zip_ref:
    zip_ref.extractall('archive/')


# Files 
filenames = os.listdir('archive')

# Dict Keys
keys = ['Filename', 'Make', 'Model', 'Year', 'MSRP', 'Front Wheel Size (in)', 'SAE Net Horsepower @ RPM',
'Displacement', 'Engine Type', 'Width, Max w/o mirrors (in)', 'Height, Overall (in)',
'Length, Overall (in)', 'Gas Mileage', 'Drivetrain', 'Passenger Capacity', 'Passenger Doors',
'Body Style']

# Pandas dataframe
df = pd.DataFrame()

# Itterate through files
for filename in filenames:
    data_row = dict(zip(keys, [filename] + filename.split('_')))
    df = df._append(data_row, ignore_index=True)