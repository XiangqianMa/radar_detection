import os

# 把以下路径更改为你的文件存放路径
# 路径文件存放路径
path_train_file = '/home/mxqian/data_convert/path_file/train'
path_val_file = '/home/mxqian/data_convert/path_file/val'
# 样本集存放路径
data_train_path = '/home/mxqian/data_convert/data/train'
data_val_path = '/home/mxqian/data_convert/data/val'

# 创建训练样本的路径文件
os.mknod(path_train_file + '/' + 'train.txt')
filename = os.listdir(data_train_path)
with open(path_train_file + '/' + 'train.txt', 'w') as f:
    for file in filename:
            if file.split('.')[1] == 'jpg':
                f.writelines(data_train_path + '/' + file + '\n')

# 创建验证样本的路径文件
os.mknod(path_val_file + '/' + 'val.txt')
filename = os.listdir(data_val_path)
with open(path_val_file + '/' + 'val.txt', 'w') as f:
    for file in filename:
            if file.split('.')[1] == 'jpg':
                f.writelines(data_val_path + '/' + file + '\n')



