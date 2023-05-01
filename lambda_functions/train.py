# Packages
import sys 
import os 
sys.path.append(os.getcwd())
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from lib.logging import *

# Check GPU is available
def lambda_hander(event,context):
    
    try:
        batch_size = 32
        img_height = 224
        img_width = 224
        seed = 123
        initial_learning_rate = 0.001
        early_stopping_patience = 5
        max_epochs = 1
    except Exception as er:
        logging.error(er)
    
    try:
        device_name = tf.config.list_physical_devices('GPU')
        if device_name == '':
            logging.error('GPU Not available')
            return
        else:
            logging.info(f'GPU Available: {device_name}')
    except Exception as er:
        logging.error(er)
        
    try:
        train_data = tf.keras.utils.image_dataset_from_directory(
            directory='data',
            batch_size=batch_size,
            validation_split=0.2,
            subset='training',
            seed=seed,
            image_size=(img_height,img_width)
        )
        validation_data = tf.keras.utils.image_dataset_from_directory(
            directory='data',
            batch_size=batch_size,
            validation_split=0.2,
            subset='validation',
            seed=seed,
            image_size=(img_height,img_width)
        )
        logging.info('Training + Validation data loaded')
    except Exception as er:
        logging.error(er)
        
    try:
        class_names = train_data.class_names
        logging.info(f'Number of classes:{len(class_names)}')
        logging.info(f'Class names:{str(class_names)}')
    except Exception as er:
        logging.error(er)
        
    try:
        resnet = tf.keras.applications.resnet.ResNet101()
        logging.info('ResNet101 loaded')
    except Exception as er:
        logging.error(er)
        
    try:
        resnet.compile(optimizer=Adam(learning_rate=initial_learning_rate),
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                    metrics=['accuracy'])
        logging.info('ResNet101 compiled.')
    except Exception as er:
        logging.error(er)
        
    try:
        early_stopping = EarlyStopping(monitor='val_loss', patience=early_stopping_patience)
        logging.info('Early stopping set.')
    except Exception as er:
        logging.error(er)
        
    try:
        logging.info('Begin Training...')
        history = resnet.fit(
            train_data,
            validation_data=validation_data,
            epochs=max_epochs,
            callbacks=[early_stopping]
        )
        n_epochs = history.params['epochs']
    except Exception as er:
        logging.error(er)
        
    try:
        path = "output/1/"
        if not os.path.exists('output'): os.mkdir('output')
        save_path = os.path.join(path)
        tf.saved_model.save(resnet, save_path)
        logging.info(f'Saved model locally to {path}')
    except Exception as er:
        logging.error(er)
        
if __name__ == "__main__":
    lambda_hander(1,1)