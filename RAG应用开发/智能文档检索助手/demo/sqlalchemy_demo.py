from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base,sessionmaker

from datetime import datetime


# 存放所有的表映射关系
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128))
    password = Column(String(128))
    create_time = Column(DateTime)
    update_time = Column(DateTime)


# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:wuzhixuan@120.76.157.51:3306/bladex')

# Base.metadata.create_all(engine)


# 创建会话
session = sessionmaker(bind=engine)

session = session()

# 新增记录
# user = User(name="张三", email="zhangsan@example.com", password="123456", create_time=datetime.now(), update_time=datetime.now())
# session.add(user)

# # 提交事务
# session.commit()


# 查询记录
users = session.query(User).all()
for user in users:
    print(user.name, user.email, user.password, user.create_time, user.update_time)


# 查询单条记录
user = session.query(User).filter(User.id == 1).first()
user.password = "1234567890"
session.commit()


# 删除记录
session.query(User).filter(User.id == 1).delete()
session.commit()