import os
import time
import datetime
from util import loggerutil


logger = loggerutil.initLogger('test_logger', 'D:\\test_logger.log')


def find_modify_file(ori_path, last_upload_time, modify_file_list=[]):
    print(ori_path)
    parents = os.listdir(ori_path)
    for parent in parents:
        child = os.path.join(ori_path, parent)
        if os.path.isdir(child):
            dir_stat = os.stat(child)
            dir_m_time = dir_stat.st_mtime
            if dir_m_time > last_upload_time:
                logger.debug("访问时间：%s", dir_stat.st_atime)
                find_modify_file(child, last_upload_time, modify_file_list)
        else:
            file_m_time = os.path.getmtime(child)
            if file_m_time > last_upload_time:
                modify_file_list.append(child)
                logger.debug("文件名：%s，修改时间：%s ", child, file_m_time)
    return modify_file_list



