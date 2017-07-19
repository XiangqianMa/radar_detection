import os
import scipy.io as sio
import numpy as np

# 从mat文件中提取原始标定信息
path = '/home/mxqian/Projects/production_practice/data/data1/condition2_1.mat'
# 从经过可视化后的图片文件中提取文件名信息
image_path = "/home/mxqian/Projects/production_practice/data_convert/data1/condition2_1"
# 存放标记文件的目录
label_file_path = "/home/mxqian/Projects/production_practice/data_convert/label_file/data1/condition2_1"
mat_file = sio.loadmat(path)
print("load mat file successfully.")
print(mat_file)


# size为图片的大小，box为标记信息
def convert(size, box):
    # 在原始标记信息中，图像宽度和图像高度是反过来的．
    width, height = size[1], size[0]
    # print(width, height)
    x, y, box_width, box_height = box[0], box[1], box[2], box[3]
    # print(x, y, box_width, box_height)
    x_convert = x/width
    y_convert = y/height
    box_width_convert = box_width/width
    box_height_convert = box_height/height
    return x_convert, y_convert, box_width_convert, box_height_convert

# 该程序块用于对原始标记信息进行归一化
size = np.shape(mat_file['source_img'])
# print(size)
target1_box = mat_file['target1'][0]
target3_1_box = mat_file['target3_1'][0]
target3_2_box = mat_file['target3_2'][0]
print(target1_box, target3_1_box, target3_2_box)
target1_box_convert = convert(size, target1_box)
target3_1_box_convert = convert(size, target3_1_box)
target3_2_box_convert = convert(size, target3_2_box)
print(target1_box_convert, target3_1_box_convert, target3_2_box_convert)

# 写入标记文件
filename = os.listdir(label_file_path)
# with open(label_file_path + '/' + filename[0], 'w') as f:
#     print(filename[0])
#     f.write(str(1) + ' ' + str(target1_box_convert[0]) + ' ' + str(target1_box_convert[1]) + ' '
#             + str(target1_box_convert[2]) + ' ' + str(target1_box_convert[3]) + '\n')
#     f.write(str(2) + ' ' + str(target2_box_convert[0]) + ' ' + str(target2_box_convert[1]) + ' '
#             + str(target2_box_convert[2]) + ' ' + str(target2_box_convert[3]))
for file in filename:
    with open(label_file_path + '/' + file, 'w') as f:
        print(file)
        f.write(str(1) + ' ' + str(target1_box_convert[0]) + ' ' + str(target1_box_convert[1]) + ' '
                + str(target1_box_convert[2]) + ' ' + str(target1_box_convert[3]) + '\n')
        f.write(str(3) + ' ' + str(target3_1_box_convert[0]) + ' ' + str(target3_1_box_convert[1]) + ' '
                + str(target3_1_box_convert[2]) + ' ' + str(target3_1_box_convert[3]) + '\n')
        f.write(str(3) + ' ' + str(target3_2_box_convert[0]) + ' ' + str(target3_2_box_convert[1]) + ' '
                + str(target3_2_box_convert[2]) + ' ' + str(target3_2_box_convert[3]))