# Packages
import os
import pandas as pd
from lib.logging import *

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