from util import ossutil, dirutil
import time
import datetime

some_conf = "../conf/someConf.ini"
cf = ossutil.get_conf_by_name(some_conf)
oss_keys = cf.options("dir")


last_time_str = cf.get("last_upload", "last_upload_time")
datetime_dt = datetime.datetime.now()  # 获取当前日期和时间
today = datetime.date.today()
today_time = time.mktime(today.timetuple())
print(today_time)


for oss_key in oss_keys:
    bucket = ossutil.get_default_bucket()
    local_path = cf.get("dir", oss_key)

    files = dirutil.find_modify_file(local_path, today_time)
    for file in files:
        print(file)
        new_oss_file = oss_key + file.replace(local_path, "")
        new_oss_file = new_oss_file.replace("\\", "/")
        print(new_oss_file)
        result = ossutil.upload_to_oss(bucket, new_oss_file, file)
        if result.status == 200:
            print("文件：" + file + " 上传成功")
