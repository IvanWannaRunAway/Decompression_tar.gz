import tarfile
import os

# 获得目录下的所有文件
def Get_file_name(file_dir):
    File = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # print(file)
            File.append(file)
    return File

# 解压缩模块
def un_tar(file_names, file_path):
    file_name = file_names
    print(file_path + file_name)
    tar = tarfile.open(file_path + file_name)
    # 更改新创建的文件夹的名字
    if file_name.find(".tar.gz") != -1:
        file_name = file_name.replace(".tar.gz", "")
    else:
        pass
    print(file_name)
    #
    if os.path.isdir(file_name):
        pass
    else:
        pass
    # os.mkdir(file_dir+"\\"+file_name)
    names = tar.getnames()
    # 循环解压缩，将压缩文件中的所有文件解压缩
    for name in names:
        print(name)
        print(file_path)
        tar.extract(name, file_path)
    return
# 获得当前的文件目录
file_dir = 'D:\\TCGAdownload\\'
print(file_dir)
files = []
files = Get_file_name('D:\\TCGAdownload\\')
print("get all file of the dir:")
# 将.tar.gz后缀的文件解压缩
print("get tar_gz file and process")
for My_file_name in files:
    print('正在解压文件：', My_file_name)
    if My_file_name.find(".tar.gz") != -1:
        # print(My_file_name)
        un_tar(My_file_name, file_dir)
    else:
        pass


