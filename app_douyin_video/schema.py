import datetime
from typing import Optional
from pydantic import BaseModel

# from schemas.base import BaseSchema


# class DouyinVideoBase(BaseSchema):
#     """douyin_video 基础"""
#     ...


# class DouyinVideoCreate(DouyinVideoBase):
#     """douyin_video 创建"""
#     ...
    

# class DouyinVideoInfo(DouyinVideoBase):
#     """douyin_video 信息"""
#     id: int
#     updated_at: Optional[datetime.datetime] = None
#     class Config(object):
#         orm_mode = True
# 这是一个dto
class DouyinDto(BaseModel):
    url:str
