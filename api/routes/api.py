from fastapi import APIRouter

from . import authentication
import app_user.api
import app_douyin_video.api # 注册小红书路由


router = APIRouter()
router.include_router(authentication.router, tags=["用户认证"], prefix="/auth")
router.include_router(app_user.api.router, tags=["用户类"], prefix="/users")

router.include_router(app_douyin_video.api.router, tags=["抖音视频图片链接提取"], prefix="/douyin_videos") # 注册视频链接

