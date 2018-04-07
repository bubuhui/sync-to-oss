__author__ = 'bubuhui'
from hashlib import md5
import os


def cal_md5_for_str(str_data):     #check string的MD5值
    m = md5()
    m.update(str_data)
    return m.hexdigest()


def cal_md5_for_file(file):         #check文件的MD5值
    stat_info = os.stat(file)
    if int(stat_info.st_size)/(1024*1024) >= 1000:
        print("File size > 1000, move to big file...")
        return cal_md5_for_big_file(file)
    m = md5()
    f = open(file, 'rb')
    m.update(f.read())
    f.close()
    return m.hexdigest()


def cal_md5_for_folder(md5_dir, md5_file):     #check文件夹的MD5值
    outfile = open(md5_file, 'w')
    for root, sub_dirs, files in os.walk(md5_dir):
        for file in files:
            file_full_path = os.path.join(root, file)
            """print file_full_path"""
            filerelpath = os.path.relpath(file_full_path, md5_dir)
            md5 = cal_md5_for_file(file_full_path)
            print(md5)
            outfile.write(filerelpath+"\t\t******-----------******\t\t"+md5+"\n")
    outfile.close()


# check大文件的MD5值
def cal_md5_for_big_file(file):
    m = md5()
    f = open(file, 'rb')
    buffer = 8192    # why is 8192 | 8192 is fast than 2048
    while 1:
        chunk = f.read(buffer)
        if not chunk:
            break
        m.update(chunk)
    f.close()
    return m.hexdigest()



