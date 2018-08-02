from util import ossutil, dirutil, md5util
import time
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import join,Table,MetaData,select,func,and_,Column,ForeignKey,Integer,String,DateTime,Text,Binary
import sys


some_conf = "../conf/someConf.ini"
cf = ossutil.get_conf_by_name(some_conf)
oss_keys = cf.options("dir")


last_time_str = cf.get("last_upload", "last_upload_time")
# 获取当前日期和时间
# datetime_dt = datetime.datetime.now()
# 设置上次
datetime_dt = datetime.date(2017, 2, 4)
# today = datetime.date.today()
# today_time = time.mktime(today.timetuple())
last_datetime = datetime.datetime.strptime(last_time_str, '%Y-%m-%d %H:%M:%S')
last_time = time.mktime(last_datetime.timetuple())
print(last_time)


Base = declarative_base()
metadata = MetaData()


class OssFile(Base):
    __tablename__ = "oss_file"
    id = Column('id', Integer, primary_key=True, nullable=True)
    md5 = Column("md5", String(64))
    oss_path = Column("oss_path", String(2000))
    local_path = Column("local_path", String(2000))
    upload_time = Column("upload_time", DateTime(), nullable=True)

eng = create_engine('sqlite:///../db/sync_to_oss.db', echo=True)
DBSession = sessionmaker(bind=eng)

for oss_key in oss_keys:
    bucket = ossutil.get_default_bucket()
    local_path = cf.get("dir", oss_key)
    files = dirutil.find_modify_file(local_path, last_time)
    for file in files:
        print(file)
        md5 = md5util.cal_md5_for_file(file)
        session = DBSession()
        # 查询MD5
        total = session.query(OssFile).filter(OssFile.md5 == md5).count()
        if total > 0:
            continue

        # new_oss_file = oss_key + file.replace(local_path, "")
        # new_oss_file = new_oss_file.replace("\\", "/")
        # new_oss_file = OssFile(id=None, md5=md5, oss_path=new_oss_file, local_path=file,
        # upload_time=datetime.datetime.now())
        # session.add(new_oss_file)
        # session.commit()
        # session.close()
        result = ossutil.upload_to_oss(bucket, new_oss_file, file)
        if result.status == 200:
            print("文件：" + file + " 上传成功")
            new_oss_file = oss_key + file.replace(local_path, "")
            new_oss_file = new_oss_file.replace("\\", "/")
            new_oss_file = OssFile(id=None, md5=md5, oss_path=new_oss_file, local_path=file,
                                   upload_time=datetime.datetime.now())
            session.add(new_oss_file)
            session.commit()
            session.close()
