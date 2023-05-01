# Packages
import os
import sys
sys.path.append(os.getcwd())
import pandas as pd
import zipfile
import shutil
from lib.logging import *

# Extract
try:
    logging.info('Starting extracting contents of archive.zip to archive/')
    with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
        zip_ref.extractall('archive/')
    logging.info('Extraction complete')
except Exception as er:
    logging.error(f'Extraction failed {er}')

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
try:
    logging.info('Starting generating metadata.csv')
    for filename in filenames:
        data_row = dict(zip(keys, [filename] + filename.split('_')))
        df = df.append(data_row, ignore_index=True)
    df.to_csv('metadata.csv')
    logging.info('metadata.csv complete')
except Exception as er:
    
    logging.error(f'Generating metadata failed {er}')
    
# Sort images into folders based on brand
for filename in filenames:
    brand = filename.split('_')[0]
    if not os.path.exists(f'data/{brand}'):
        os.makedirs(f'data/{brand}')
    try:
        shutil.move(src=f'archive/{filename}', dst=f'data/{brand}/{filename}')
    except:
        logging.warn(f'Cant find {filename}')