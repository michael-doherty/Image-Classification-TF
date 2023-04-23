from kaggle.api.kaggle_api_extended import KaggleApi
from lib.logging import *
import boto3
import tempfile
from dotenv import load_dotenv
load_dotenv()

def lambda_handler(event, context):
    logging.info(f'event:{event}')
    logging.info(f'context:{context}')
    
    try:
        s3_client = boto3.client('s3')
    except Exception as er:
        logging.error(er)
    try:
        kaggle = KaggleApi()
        kaggle.authenticate()
    except Exception as er:
        logging.error(er)

    try:
        temp_dir = tempfile.TemporaryDirectory()
    except Exception as er:
        logging.error(er)
    
    try:
        kaggle.dataset_download_files('prondeau/the-car-connection-picture-dataset', path=temp_dir.name)
    except Exception as er:
        logging.error(er)
        raise

    try:
        #upload to s3 bucket
        print()
    except Exception as er:
        logging.error(er)