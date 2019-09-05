# reads the names of the train balanced subsample and unzips train images into the '../input/train/' folder

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
print(os.listdir("../input"))
import sys
import matplotlib.pyplot as plt
sys.path.append('rxrx1-utils')
if 'google.colab' in sys.modules:
    #!git clone https://github.com/recursionpharma/rxrx1-utils
    sys.path.append('/content/rxrx1-utils')

import rxrx.io as rio
#!git clone https://github.com/recursionpharma/rxrx1-utils

# Load the Pandas libraries with alias 'pd'
import pandas as pd

import zipfile

# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("../input/balanced_sample_train.csv")
# Preview the first 5 lines of the loaded data
print(data.head())
print(data.shape)
#(36515, 5)
#(512, 512, 3)

my_zip =  zipfile.ZipFile('../input/train.zip') # Specify your zip file's name here
storage_path = '../input/train'
#
# y = rio.load_site_as_rgb('train', 'HEPG2-01', 1, 'C11', 1, (1, 2, 3, 4, 5, 6), storage_path)
# print(y.shape)
# print(y)
# plt.figure(figsize=(8, 8))
# plt.axis('off')
#
# _ = plt.imshow(y)
# plt.show()

print(len(data))

for i in range(len(data)):
    print(i)

    data_filename = str(data.iloc[i,1])+'/Plate'+str(data.iloc[i,2])+'/'+ str(data.iloc[i,3])
    # print(data_filename)
    for file in my_zip.namelist():

        if my_zip.getinfo(file).filename.startswith(data_filename):
            my_zip.extract(file, storage_path) # extract the file to current folder if it is a text file


