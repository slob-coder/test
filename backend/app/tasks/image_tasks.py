"""
图片生成任务

异步调用 AI 服务生成分镜图片。
"""

from typing import Any

from app.tasks.celery_app import celery_app


@celery_app.task(bind=True, name="image.generate_single", max_retries=3)
def generate_single_image_task(
    self,
    storyboard_item_id: str,
    prompt: str,
    style: str = "realistic",
) -> dict[str, Any]:
    """
    异步生成单个分镜图片
    
    Args:
        storyboard_item_id: 分镜项 ID
        prompt: 图片生成提示词
        style: 图片风格
        
    Returns:
        生成的图片信息
    """
    # TODO: 实现 AI 图片生成逻辑
    # 1. 调用图片生成服务 (DALL-E / Stable Diffusion)
    # 2. 下载生成的图片
    # 3. 上传到 MinIO
    # 4. 更新数据库记录
    # 5. 推送 SSE 进度事件
    raise NotImplementedError("图片生成任务待实现")


@celery_app.task(bind=True, name="image.generate_batch", max_retries=3)
def generate_batch_images_task(
    self,
    project_id: str,
    items: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    批量生成分镜图片
    
    Args:
        project_id: 项目 ID
        items: 分镜项列表，每项包含 id 和 prompt
        
    Returns:
        批量生成结果
    """
    # TODO: 实现批量图片生成逻辑
    # 1. 遍历分镜项
    # 2. 并发调用图片生成服务
    # 3. 汇总结果
    raise NotImplementedError("批量图片生成任务待实现")
