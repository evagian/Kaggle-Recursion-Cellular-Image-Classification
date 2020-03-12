
# Kaggle-Recursion-Cellular-Image-Classification
Run python files with the given order:

### 1_balanced_subsample.py
Splits train and test set using balanced subsamples containing images from all 1108 classes

### 2a_unzip_images_train.py
Reads the names of the train balanced subsample and unzips train images into the '../input/train/' folder

### 2b_unzip_images_test.py
Reads the names of the test balanced subsample and unzips test images into the '../input/test/' folder

# Data structure 

We are going to use ResNet50 pretrained weights. 
To train ResNet50 succesfully, our input data should have the following structure

![alt text](https://github.com/evagian/Kaggle-Recursion-Cellular-Image-Classification/blob/master/figures/data-structure.png)

The following 2 files organize input images using the data structure shown above 

### 3a_preprocessing_train.py

### 3b_preprocessing_test.py

# Train ResNet50 
Transfer learning: Initialize network weights using ResNet50 trained weights and train model on Kaggle's ["Recursion Cellular Image Classification"](https://www.kaggle.com/c/recursion-cellular-image-classification/overview) dataset

### 4_train_resnet50.ipynb
Train ResNet50

