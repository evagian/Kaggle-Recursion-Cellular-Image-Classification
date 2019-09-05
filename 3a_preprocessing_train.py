import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
print(os.listdir("../input"))
import sys
import matplotlib.pyplot as plt
sys.path.append('rxrx1-utils')
from tqdm import tqdm
from PIL import Image
import rxrx.io as rio
#!git clone https://github.com/recursionpharma/rxrx1-utils
import zipfile

# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
data = pd.read_csv("../input/balanced_sample_train.csv")
# Preview the first 5 lines of the loaded data
print(data.head())
#
# # pos_control = data[data['well_type']=='positive_control']
# # print(pos_control.head())
# #
# # well_type = 'positive_control'
#
# filename = "../input/train.csv"
# data = pd.read_csv(filename)

# data = data[data['well_type'] == well_type]
print((data.shape))

storage_path = '../input/train'


def convert_to_rgb(df, split, resize=False, new_size=224, extension='png'):
    RGB_MAP = {
        1: {
            'rgb': np.array([19, 0, 249]),
            'range': [0, 51]
        },
        2: {
            'rgb': np.array([42, 255, 31]),
            'range': [0, 107]
        },
        3: {
            'rgb': np.array([255, 0, 25]),
            'range': [0, 64]
        },
        4: {
            'rgb': np.array([45, 255, 252]),
            'range': [0, 191]
        },
        5: {
            'rgb': np.array([250, 0, 253]),
            'range': [0, 89]
        },
        6: {
            'rgb': np.array([254, 255, 40]),
            'range': [0, 191]
        }
    }

    N = df.shape[0]

    print(df.head())
    print(df['id_code'].iloc[1])
    for i in tqdm(range(N)):

        code = df['id_code'].iloc[i]
        experiment = df['experiment'].iloc[i]
        plate = df['plate'].iloc[i]
        well = df['well'].iloc[i]
        sirna = df['sirna'].iloc[i]

        for site in [1, 2]:

            folder = '../input/'+str(split)+'/'+str(sirna)+'/'

            if not os.path.exists(folder):
                os.makedirs(folder)

            save_path = '../input/'+str(split)+'/'+str(sirna)+'/'+str(code)+'_s'+str(site)+'.'+str(extension)

            im = rio.load_site_as_rgb(
                split, experiment, plate, well, site, channels=(1, 2, 3, 4, 5, 6),
                base_path='../input/', rgb_map=RGB_MAP
            )
            im = im.astype(np.uint8)
            im = Image.fromarray(im)

            if resize:
                im = im.resize((new_size, new_size), resample=Image.BILINEAR)

            im.save(save_path)




def build_new_df(df, extension='.png'):
    new_df = pd.concat([df, df])
    new_df['filename'] = pd.concat([
        df['id_code'].apply(lambda string: string + '_s1' ),
        df['id_code'].apply(lambda string: string + '_s2' )

    ])

    new_df['filename'] = new_df['filename'] + "_" + new_df["sirna"].map(str) + str(extension)


    return new_df


def zip_and_remove(path):
    ziph = zipfile.ZipFile(str(path)+'.zip', 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file in tqdm(files):
            file_path = os.path.join(root, file)
            ziph.write(file_path)
            os.remove(file_path)

    ziph.close()

convert_to_rgb(data, 'train')
zip_and_remove('train')

new_train = build_new_df(data)
new_train.to_csv('../input/balanced_sample_new_train.csv', index=False)




