import os
import scipy.io as sio
import numpy as np

# 从mat文件中提取原始标定信息
path = '/home/mxqian/Projects/production_practice/data/data1/condition2_1.mat'
# 从经过可视化后的图片文件中提取文件名信息
image_path_train = "/home/mxqian/Projects/production_practice_2/data/train"
image_path_val = "/home/mxqian/Projects/production_practice_2/data/val"
# 存放标记文件的目录
label_file_path_train = "/home/mxqian/Projects/production_practice_2/data/train"
label_file_path_val = "/home/mxqian/Projects/production_practice_2/data/val"

mat_file = sio.loadmat(path)
print("load mat file successfully.")
# print(mat_file)


# size为图片的大小，box为标记信息
def convert(size, box):
    # 在原始标记信息中，图像宽度和图像高度是反过来的．
    width, height = size[1], size[0]
    x, y, box_width, box_height = box[0], box[1], box[2], box[3]
    # voc数据集采用的是图像的中点坐标占整个图像的比例
    x_convert = x/width
    y_convert = y/height
    box_width_convert = box_width/width
    box_height_convert = box_height/height
    return x_convert, y_convert, box_width_convert, box_height_convert

# 该程序块用于对原始标记信息进行归一化
size = np.shape(mat_file['source_img'])
target1_box = mat_file['target1']
target3_1_box = mat_file['target3_1']
target3_2_box = mat_file['target3_2']
target3_3_box = mat_file['target3_3']
target3_4_box = mat_file['target3_4']

# 该数据集每张图片都有着不同的标记，所以对于每个目标都使用二维数组进行存储
target1_box_convert = np.zeros((np.shape(target1_box)[0], np.shape(target1_box)[1]))
for i in range(np.shape(target1_box)[0]):
    target1_box_convert[i] = convert(size, target1_box[i])

target3_1_box_convert = np.zeros((np.shape(target3_1_box)[0], np.shape(target3_1_box)[1]))
for i in range(np.shape(target3_1_box)[0]):
    target3_1_box_convert[i] = convert(size, target3_1_box[i])

target3_2_box_convert = np.zeros((np.shape(target3_2_box)[0], np.shape(target3_2_box)[1]))
for i in range(np.shape(target3_2_box)[0]):
    target3_2_box_convert[i] = convert(size, target3_2_box[i])

target3_3_box_convert = np.zeros((np.shape(target3_3_box)[0], np.shape(target3_3_box)[1]))
for i in range(np.shape(target3_3_box)[0]):
    target3_3_box_convert[i] = convert(size, target3_3_box[i])

target3_4_box_convert = np.zeros((np.shape(target3_4_box)[0], np.shape(target3_4_box)[1]))
for i in range(np.shape(target3_4_box)[0]):
    target3_4_box_convert[i] = convert(size, target3_4_box[i])


# # 创建标记文件（空文件）
# image_filename = os.listdir(image_path)
# # 将样本名称抽取出来，创建同名.txt文件，用于存放标记信息
# for file in image_filename:
#     file = file.split('.')[0]
#     os.mknod(label_file_path + "/" + file + '.txt')

# 写入标记文件
for file in range(np.shape(target1_box)[0]):
    i = file
    file = str(121) + str(file + 1)
    if os.path.exists(label_file_path_train + '/' + file + '.txt'):
        with open(label_file_path_train + '/' + file + '.txt', 'w') as f:
            print(file, '.txt train')
            f.write(str(0) + ' ' + str(target1_box_convert[i][0]) + ' ' + str(target1_box_convert[i][1]) + ' '
                    + str(target1_box_convert[i][2]) + ' ' + str(target1_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_1_box_convert[i][0]) + ' ' + str(target3_1_box_convert[i][1]) + ' '
                    + str(target3_1_box_convert[i][2]) + ' ' + str(target3_1_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_2_box_convert[i][0]) + ' ' + str(target3_2_box_convert[i][1]) + ' '
                    + str(target3_2_box_convert[i][2]) + ' ' + str(target3_2_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_3_box_convert[i][0]) + ' ' + str(target3_3_box_convert[i][1]) + ' '
                    + str(target3_3_box_convert[i][2]) + ' ' + str(target3_3_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_4_box_convert[i][0]) + ' ' + str(target3_4_box_convert[i][1]) + ' '
                    + str(target3_4_box_convert[i][2]) + ' ' + str(target3_4_box_convert[i][3]) + '\n')
    elif os.path.exists(label_file_path_val + '/' + file + '.txt'):
        with open(label_file_path_val + '/' + file + '.txt', 'w') as f:
            print(file, '.txt val')
            f.write(str(0) + ' ' + str(target1_box_convert[i][0]) + ' ' + str(target1_box_convert[i][1]) + ' '
                    + str(target1_box_convert[i][2]) + ' ' + str(target1_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_1_box_convert[i][0]) + ' ' + str(target3_1_box_convert[i][1]) + ' '
                    + str(target3_1_box_convert[i][2]) + ' ' + str(target3_1_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_2_box_convert[i][0]) + ' ' + str(target3_2_box_convert[i][1]) + ' '
                    + str(target3_2_box_convert[i][2]) + ' ' + str(target3_2_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_3_box_convert[i][0]) + ' ' + str(target3_3_box_convert[i][1]) + ' '
                    + str(target3_3_box_convert[i][2]) + ' ' + str(target3_3_box_convert[i][3]) + '\n')
            f.write(str(2) + ' ' + str(target3_4_box_convert[i][0]) + ' ' + str(target3_4_box_convert[i][1]) + ' '
                    + str(target3_4_box_convert[i][2]) + ' ' + str(target3_4_box_convert[i][3]) + '\n')
