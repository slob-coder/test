"""
Celery 应用配置

任务队列配置，支持异步脚本生成、图片生成、视频合成等任务。
"""

from celery import Celery

from app.config import settings

celery_app = Celery(
    "aivideo",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        "app.tasks.script_tasks",
        "app.tasks.image_tasks",
        "app.tasks.video_tasks",
        "app.tasks.compose_tasks",
    ],
)

# Celery 配置
celery_app.conf.update(
    # 任务序列化
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    
    # 时区
    timezone="Asia/Shanghai",
    enable_utc=True,
    
    # 任务结果配置
    result_expires=3600,  # 结果保留 1 小时
    
    # 任务超时配置
    task_soft_time_limit=300,  # 软超时 5 分钟
    task_time_limit=600,  # 硬超时 10 分钟
    
    # 重试配置
    task_default_retry_delay=10,
    task_max_retries=3,
    
    # Worker 配置
    worker_prefetch_multiplier=1,
    worker_concurrency=4,
)

# 任务路由
celery_app.conf.task_routes = {
    "app.tasks.script_tasks.*": {"queue": "script"},
    "app.tasks.image_tasks.*": {"queue": "image"},
    "app.tasks.video_tasks.*": {"queue": "video"},
    "app.tasks.compose_tasks.*": {"queue": "compose"},
}
