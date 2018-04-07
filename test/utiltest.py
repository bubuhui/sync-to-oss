from util import md5util
import sqlite3
import sqlalchemy
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import join,Table,MetaData,select,func,and_,Column,ForeignKey,Integer,String,DateTime,Text,Binary
from sqlalchemy.orm import deferred,mapper,relationship,column_property,object_session,validates




# md5util.cal_md5_for_folder(r'F:\工作\Wish20170518', r'F:\a.txt')


Base = declarative_base()
metadata = MetaData()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class OssFile(Base):
    __tablename__ = "oss_file"
    id = Column('id', Integer, primary_key=True, nullable=True)
    md5 = Column("md5", String(64))
    oss_path = Column("oss_path", String(2000))
    local_path = Column("local_path", String(2000))
    upload_time = Column("upload_time", DateTime(), nullable=True)


eng = create_engine('sqlite:///../db/test2.db', echo=True)
DBSession = sessionmaker(bind=eng)
# 创建session对象:
session = DBSession()
# 创建新User对象:
md52 = "dd222ddadss"
# user = User(id='133', name='333')
new_oss_file = OssFile(id=None, md5=md52, oss_path="o2ss_path", local_path="local_path", upload_time=datetime.datetime.now())
# 添加到session:
session.add(new_oss_file)
# 提交即保存到数据库:
session.commit()
# # 关闭session:
session.close()


# 创建Session:
# session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id == '1').one()
# # 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# # 关闭Session:
# session.close()

# conn = sqlite3.connect('./db/sync_to_oss.db')
# cursor = conn.cursor()
# cursor.execute('create table oss_file (id integer PRIMARY KEY autoincrement, md5 varchar(64), '
#                'oss_path varchar(2000), local_path varchar(2000), upload_time datetime default (datetime('now', 'localtime')))')
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()
