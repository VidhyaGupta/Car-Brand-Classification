import os
import numpy as np
import shutil

# # Creating Train / Test folders (One time use)
img_dir = 'Image_Folder'
clsList = os.listdir(img_dir + "/")

train_dir = 'Datasets/Train/'
test_dir = 'Datasets/Test/'

SPLIT_SIZE = 60     #training data size

for cls in clsList:
    src_dir = img_dir + '/' + cls  # Folder to copy images from
    out_train_dir = train_dir + cls
    out_test_dir = test_dir + cls

    if not os.path.exists(out_train_dir):
        os.makedirs(out_train_dir)
    if not os.path.exists(out_test_dir):
        os.makedirs(test_dir + cls)
    allFileNames = os.listdir(src_dir)
    print(allFileNames)
    train_filenames, test_filenames = np.split(np.array(allFileNames), [SPLIT_SIZE])

    train_filenames = [src_dir + '/' + name for name in train_filenames.tolist()]
    test_filenames = [src_dir + '/' + name for name in test_filenames.tolist()]

    # Copy-Pasting Images
    for name in train_filenames:
        shutil.copy(name, out_train_dir)
    for name in test_filenames:
        shutil.copy(name, out_test_dir)

print("Splitting of folder is done")