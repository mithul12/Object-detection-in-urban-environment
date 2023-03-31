import argparse
import glob
import os
import shutil
import random

import numpy as np

from utils import get_module_logger


def split():
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    filenames = os.listdir("/home/workspace/data/waymo/training_and_validation")

    #Shuffle tf records list
    np.random.shuffle(filenames)
    
    #Train size: 90%, validation size: 10%
    train_size = int(0.9 * len(filenames))
    val_size = len(filenames) - train_size
    
    train_filenames, val_filenames = np.split(filenames, [train_size])
    
    source_folder = "/home/workspace/data/waymo/training_and_validation/"
    
    train_folder = "/home/workspace/data/waymo/train/"
    #Move training records
    for filename in train_filenames:
        shutil.move(source_folder+filename, train_folder+filename)
        
    val_folder = "/home/workspace/data/waymo/val/"
    #Move validation records
    for filename in val_filenames:
        shutil.move(source_folder+filename, val_folder+filename)
    
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split()
