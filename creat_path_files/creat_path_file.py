import os

path_train_file = '/home/mxqian/Projects/production_practice/data_convert/path_file/train'
path_val_file = '/home/mxqian/Projects/production_practice/data_convert/path_file/val'
data_train_path = '/home/mxqian/Projects/production_practice/data_convert/data/train'
data_val_path = '/home/mxqian/Projects/production_practice/data_convert/data/val'

os.mknod(path_val_file + '/' + 'val.txt')
filename = os.listdir(data_val_path)
with open(path_val_file + '/' + 'val.txt', 'w') as f:
    for file in filename:
            f.writelines(data_val_path + '/' + file + '\n')




