# -*- coding: utf-8 -*-
import oss2
import configparser
from util import loggerutil


some_conf = "conf/someConf.ini"


# 读取配置文件
def get_conf_by_name(conf_name):
    cf = configparser.ConfigParser()
    cf.read(conf_name, encoding="utf-8-sig")
    local_conf = cf.get("conf_path", "conf_path")
    if local_conf:
        cf.read(local_conf, encoding="utf-8-sig")
    return cf


# 获取默认配置信息
def get_default_bucket():
    cf = get_conf_by_name(some_conf)
    # 先读一下配置文件

    access_key_id = cf.get('aliyun', 'access_key_id')
    access_key_secret = cf.get('aliyun', 'access_key_secret')
    endpoint = cf.get("aliyun", "endpoint")
    bucket_name = cf.get("aliyun", "bucket_name")
    auth = oss2.Auth(access_key_id, access_key_secret)
    my_bucket = oss2.Bucket(auth, endpoint, bucket_name)
    return my_bucket


def upload_to_oss(oss_bucket, oss_dir, local_file):
    result = oss2.resumable_upload(oss_bucket, oss_dir, local_file, multipart_threshold=100 * 1024)
    # print('http status: {0}'.format(result.status))
    # print('request_id: {0}'.format(result.request_id))
    # print('ETag: {0}'.format(result.etag))
    # print('date: {0}'.format(result.headers['date']))
    return result


