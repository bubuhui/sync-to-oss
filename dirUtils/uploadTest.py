# -*- coding: utf-8 -*-
import os
import oss2
import configparser


some_conf = "../conf/someConf.ini"


# 读取配置文件
def get_conf_by_name(conf_name):
    cf = configparser.ConfigParser()
    cf.read(conf_name, encoding="utf-8-sig")
    return cf


# 获取默认配置信息
def get_default_bucket():
    cf = get_conf_by_name(some_conf)
    access_key_id = cf.get('aliyun', 'access_key_id')
    access_key_secret = cf.get('aliyun', 'access_key_secret')
    endpoint = cf.get("aliyun", "endpoint")
    bucket_name = cf.get("aliyun", "bucket_name")
    auth = oss2.Auth(access_key_id, access_key_secret)
    my_bucket = oss2.Bucket(auth, endpoint, bucket_name)
    return my_bucket


def upload_to_oss(oss_bucket, oss_dir, local_dir, local_file):
    result = oss2.resumable_upload(oss_bucket, oss_dir, local_file, multipart_threshold=100 * 1024)
    # print('http status: {0}'.format(result.status))
    # print('request_id: {0}'.format(result.request_id))
    # print('ETag: {0}'.format(result.etag))
    # print('date: {0}'.format(result.headers['date']))
    return result


def list_dir(dir_path):
    print(dir_path)
    for child_dir in os.listdir(dir_path):
        child_dir_path = os.path.join(dir_path, child_dir)
        print(child_dir_path)
        if os.path.isdir(child_dir_path):
            list_dir(child_dir_path)


cf = get_conf_by_name(some_conf)
dirs = cf.options("dir")
for thisdir in dirs:
    print(thisdir)
    bucket = get_default_bucket()
    local_dir = cf.get("dir", thisdir)
    list_dir(local_dir)



# with open("d:/oss/test.txt", "rb") as fileObj:
#     result = bucket.put_object("test2.txt", fileObj)
#     print('http status: {0}'.format(result.status))
#     print('request_id: {0}'.format(result.request_id))
#     print('ETag: {0}'.format(result.etag))
#     print('date: {0}'.format(result.headers['date']))
