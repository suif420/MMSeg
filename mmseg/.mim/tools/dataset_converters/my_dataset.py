# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import gzip
import os
import shutil


def un_gz(src, dst):
    g_file = gzip.GzipFile(src)
    with open(dst, 'wb+') as f:
        f.write(g_file.read())
    g_file.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert STARE datasets to mmsegmentation format')
    parser.add_argument('--image_path', help='the path of image_path',default='I:\experiment\AMMSeg\data\my_dataset_origin\Images')
    parser.add_argument('--text_path', help='the path of text',default='I:\experiment\AMMSeg\data\my_dataset_origin\ImageSets\Segmentation')
    parser.add_argument('--output_path',help='the path of output',default='I:\experiment\AMMSeg\data\my_dataset')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    image_path = args.image_path
    text_path = args.text_path
    output_path = args.output_path
    print('Making directories...')

    with open(os.path.join(text_path,'train.txt'),'r') as f:
        file_names = f.readlines()
        for file_name in file_names:
            train_image_path_old = os.path.join(image_path+'/img/',file_name.strip())
            train_label_path_old = os.path.join(image_path+'/lab/',file_name.strip())
            train_image_path_new = output_path+'/img_dir/train'
            train_label_path_new = output_path+'/ann_dir/train'
            shutil.copy(train_image_path_old,train_image_path_new)
            shutil.copy(train_label_path_old,train_label_path_new)

    with open(os.path.join(text_path, 'val.txt'), 'r') as f:
        file_names = f.readlines()
        for file_name in file_names:
            train_image_path_old = os.path.join(image_path + '/img/', file_name.strip())
            train_label_path_old = os.path.join(image_path + '/lab/', file_name.strip())
            train_image_path_new = output_path + '/img_dir/val'
            train_label_path_new = output_path + '/ann_dir/val'
            shutil.copy(train_image_path_old, train_image_path_new)
            shutil.copy(train_label_path_old, train_label_path_new)

    print('Done!')


if __name__ == '__main__':

    main()