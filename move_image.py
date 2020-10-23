import os
from shutil import copyfile
f = open(r"E:\2020program\yolov5-master\data\ImageSets\test"
         r".txt")#test.txt to  val
line = f.readline()
print(line)
path = r"E:\2020program\yolov5-master\data\images"
out_path = r"E:\2020program\yolov5-master\data\images\test"
while line:
    copyfile(os.path.join(path,line.strip()+".jpg"),os.path.join(out_path,line.strip()+".jpg"))####
    line = f.readline()
f.close()



