import os
import numpy as np
import random
import shutil
import re

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def data_structuring(base_dir, division):

    dirs = os.listdir(base_dir)
    num_classes = len(dirs)

    random.seed(1234)
    train_inds = []

    temp = list(range(1, num_classes + 1))
    random.shuffle(temp)

    train_inds = temp[0:division['train']]
    val_inds = temp[division['train'] : division['train'] + division['validation']]
    test_inds = temp[division['train'] + division['validation'] : num_classes + 1]

    train_inds.sort()
    val_inds.sort()
    test_inds.sort()

    train_dirs = [dirs[i-1] for i in train_inds]
    val_dirs = [dirs[i-1] for i in val_inds]
    test_dirs = [dirs[i-1] for i in test_inds]


    return {'train':train_dirs, 'validation':val_dirs, 'test':test_dirs}


def oxford_partitioning(dir, division):
    base_dir = os.path.join(dir, 'images')
    images = os.listdir(base_dir)

    catsdir = os.path.join(base_dir, 'cats')

    sum = 0
    cats = ['Abyssinian', 'Bengal', 'Birman', 'Bombay', 'British_Shorthair', 'Egyptian_Mau', 'Maine_Coon', 'Persian', 'Ragdoll', 'Russian_Blue', 'Siamese', 'Sphynx']
    for image in images:
        if 'A' <= image[0] <= 'Z':
            cat_name = re.findall('[A-Z]+[a-z]*_*[A-Z]*[a-z]*', image)

            if cat_name[0][-1] is '_':
                cat_name = cat_name[0][0:-1]
            else:
                cat_name = cat_name[0]
            # if cat_name not in cats:
            #     cats.append(cat_name)
            #     sum += 1

            old_path = os.path.join('data', 'oxford', 'images', image)
            new_path = os.path.join('data', 'oxford', 'images', 'cats', cat_name, image)
            os.rename(old_path, new_path)
            a = 1

    sum = 0
    dogs = ['american_bulldog', 'american_pit_bull_terrier', 'basset_hound', 'beagle', 'boxer', 'chihuahua', 'english_cocker_spaniel', 'english_setter', 'german_shorthaired', 'great_pyrenees', 'havanese', 'japanese_chin', 'keeshond', 'leonberger', 'miniature_pinscher', 'newfoundland', 'pomeranian', 'pug', 'saint_bernard', 'samoyed', 'scottish_terrier', 'shiba_inu', 'staffordshire_bull_terrier', 'wheaten_terrier', 'yorkshire_terrier']
    for image in images:
        if 'a' <= image[0] <= 'z':
            dog_name = re.findall('[a-z]+[_[a-z]+]*', image)
            a=1
            if dog_name[0][-1] is '_':
                dog_name = dog_name[0][0:-1]
            else:
                dog_name = dog_name[0]
            # if dog_name not in dogs:
            #     dogs.append(dog_name)
            #     sum += 1

            if dog_name == 'cats' or dog_name == 'dogs':
                continue
            old_path = os.path.join('data', 'oxford', 'images', image)
            new_path = os.path.join('data', 'oxford', 'images', 'dogs', dog_name, image)
            os.rename(old_path, new_path)
            a = 1
    # for dog in dogs:
    #     os.mkdir(os.path.join('data', 'oxford', 'images', 'dogs', dog))

    print(dogs)
    print(sum)

if __name__ == '__main__':
    stanford_path = os.path.join('data', 'stanford', 'images')
    stanford_division = {'train':80, 'validation':20, 'test':20}
    # stanford_images_dirs = data_structuring(stanford_path, stanford_division)

    oxford_path = os.path.join('data', 'oxford', 'images', 'dogs')
    oxford_division = {'train': 15, 'validation':0, 'test': 10}
    oxford_images_dirs = data_structuring(oxford_path, oxford_division)

    a = 1