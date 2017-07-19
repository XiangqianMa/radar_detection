import os
import scipy.io as sio
import numpy as np

# 从mat文件中提取原始标定信息
path = '/home/mxqian/Projects/production_practice/data/data3/target1+2/target2_1/data25_1.mat'
# 从经过可视化后的图片文件中提取文件名信息
image_path = "/home/mxqian/Projects/production_practice/data_convert/data3/target1+2/target2_1/data25_1"
# 存放标记文件的目录
label_file_path = "/home/mxqian/Projects/production_practice/data_convert/label_file/data3/target1+2/target2_1/data25_1"
mat_file = sio.loadmat(path)
print("load mat file successfully.")
print(mat_file)


# size为图片的大小，box为标记信息
def convert(size, box):
    # 在原始标记信息中，图像宽度和图像高度是反过来的．
    width, height = size[1], size[0]
    x, y, box_width, box_height = box[0], box[1], box[2], box[3]
    x_convert = x/width
    y_convert = y/height
    box_width_convert = box_width/width
    box_height_convert = box_height/height
    return x_convert, y_convert, box_width_convert, box_height_convert

# 该程序块用于对原始标记信息进行归一化
size = np.shape(mat_file['source_img'])
# print(size)
target1_box = mat_file['target1']
# target2_box = mat_file['target2']
# print(target1_box, target3_box)

# 该数据集每张图片都有着不同的标记，所以对于每个目标都使用二维数组进行存储
target1_box_convert = np.zeros((np.shape(target1_box)[0], np.shape(target1_box)[1]))
for i in range(np.shape(target1_box)[0]):
    target1_box_convert[i] = convert(size, target1_box[i])
# print(target1_box_convert)
# target2_box_convert = np.zeros((np.shape(target2_box)[0], np.shape(target2_box)[1]))
# for i in range(np.shape(target2_box)[0]):
#     target2_box_convert[i] = convert(size, target2_box[i])
# print(target3_box_convert)

# 创建标记文件（空文件）
image_filename = os.listdir(image_path)
# 将样本名称抽取出来，创建同名.txt文件，用于存放标记信息
for file in image_filename:
    file = file.split('.')[0]
    os.mknod(label_file_path + "/" + file + '.txt')

# 写入标记文件
for file in range(np.shape(target1_box)[0]):
    i = file
    file = str('31221251') + str(file + 1)
    with open(label_file_path + '/' + file + '.txt', 'w') as f:
        print(file, '.txt')
        f.write(str(1) + ' ' + str(target1_box_convert[i][0]) + ' ' + str(target1_box_convert[i][1]) + ' '
                + str(target1_box_convert[i][2]) + ' ' + str(target1_box_convert[i][3]))
        # f.write(str(2) + ' ' + str(target2_box_convert[i][0]) + ' ' + str(target2_box_convert[i][1]) + ' '
        #         + str(target2_box_convert[i][2]) + ' ' + str(target2_box_convert[i][3]))

