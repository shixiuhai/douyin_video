from typing import List, Any, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
# from .schema import DouyinVideoCreate, DouyinVideoInfo
# from .model import DouyinVideo
from .schema import DouyinDto
from core.logger import logger
from lib.jwt import get_current_user
from app_user.model import User

from .douyin_video_parse import add


router = APIRouter()


"""
接口：DouyinVideo 表增删改查

POST   /api/douyin_videos            ->  create_douyin_video  ->  创建 douyin_video
GET    /api/douyin_videos            ->  get_douyin_videos    ->  获取所有 douyin_video
GET    /api/douyin_videos/{douyin_video_id}   ->  get_douyin_video     ->  获取单个 douyin_video
PUT    /api/douyin_videos/{douyin_video_id}   ->  update_douyin_video  ->  更新单个 douyin_video
DELETE /api/douyin_videos/{douyin_video_id}   ->  delete_douyin_video  ->  删除单个 douyin_video
"""
@router.post("/video_parse" , name="抖音视频或者图片链接解析")
async def create_douyin_video(douyin_dto: DouyinDto, db: Session = Depends(get_db)):
    logger.info("请求成功")
    return {
        "code":200,
        "data":{"parse_url":douyin_dto.url},
        "message":"成功",
        "add":add()
    }
    
@router.post("/video_parse_token" , name="抖音视频或者图片链接解析")
async def create_douyin_video(douyin_dto: DouyinDto, current_user: User = Depends(get_current_user)):
    logger.info("请求成功")
    return {
        "code":200,
        "data":{"parse_url":douyin_dto.url},
        "message":"成功",
        "add":add()
    }



# # 新建 douyin_video
# @router.post("/", response_model=DouyinVideoInfo, name="新建 douyin_video")
# async def create_douyin_video(douyin_video: DouyinVideoCreate, db: Session = Depends(get_db)):
#     return DouyinVideo.create(db)


# # 获取所有 douyin_video
# @router.get("/", response_model=List[DouyinVideoInfo], name="获取所有 douyin_video")
# async def get_douyin_videos(db: Session = Depends(get_db)):
#     return DouyinVideo.all(db)


# # 通过id查询 douyin_video
# @router.get("/{douyin_video_id}", response_model=Union[DouyinVideoInfo, Any], name="查询 douyin_video by douyin_video_id")
# async def get_douyin_video(douyin_video_id: int, db: Session = Depends(get_db)):
#     db_douyin_video = DouyinVideo.get_or_404(db, id=douyin_video_id)
#     if not db_douyin_video:
#         raise HTTPException(status_code=404, detail="DouyinVideo not found")
#     return db_douyin_video


# # 通过id更改 douyin_video
# @router.put("/{douyin_video_id}", name="更改 douyin_video by douyin_video_id")
# async def update_douyin_video(douyin_video_id: int, douyin_video: DouyinVideoCreate, db: Session = Depends(get_db)):
#     return DouyinVideo.update_by(db, douyin_video_id, {})


# # 通过id删除 douyin_video
# @router.delete("/{douyin_video_id}", name="删除 douyin_video by douyin_video_id")
# async def delete_douyin_video(douyin_video_id: int, db: Session = Depends(get_db)):
#     DouyinVideo.remove_by(db, id=douyin_video_id)
#     return 0
