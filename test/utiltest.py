from util import md5util
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import join,Table,MetaData,select,func,and_,Column,ForeignKey,Integer,String,Text,Binary
from sqlalchemy.orm import deferred,mapper,relationship,column_property,object_session,validates




# md5util.cal_md5_for_folder(r'F:\工作\Wish20170518', r'F:\a.txt')


Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


eng = create_engine('sqlite:///test.db', echo=True)
DBSession = sessionmaker(bind=eng)
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='6', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '1').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

# conn = sqlite3.connect('./db/test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()
