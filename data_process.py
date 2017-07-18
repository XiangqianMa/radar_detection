import os


files = os.listdir("/home/mxqian/Projects/production_practice/data_convert/data4")
for i in files:
    os.mkdir("/home/mxqian/Projects/production_practice/data_convert/label_file/data4/" + i)