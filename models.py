from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True) # 设置主键和索引
    title = Column(String(32))
    content = Column(String(32))
    pulished = Column(Boolean)
