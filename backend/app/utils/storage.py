"""
存储工具模块 - MinIO 操作封装
"""

from typing import Optional
from pathlib import Path


class StorageClient:
    """MinIO 存储客户端"""
    
    def __init__(self):
        # TODO: 初始化 MinIO 客户端
        raise NotImplementedError("MinIO 客户端初始化待实现")
    
    async def upload_file(
        self, 
        file_path: Path, 
        object_name: str,
        content_type: Optional[str] = None
    ) -> str:
        """上传文件到 MinIO"""
        # TODO: 实现文件上传逻辑
        raise NotImplementedError("文件上传逻辑待实现")
    
    async def download_file(self, object_name: str, local_path: Path) -> None:
        """从 MinIO 下载文件"""
        # TODO: 实现文件下载逻辑
        raise NotImplementedError("文件下载逻辑待实现")
    
    async def get_file_url(self, object_name: str, expires: int = 3600) -> str:
        """获取文件访问 URL"""
        # TODO: 实现获取文件 URL 逻辑
        raise NotImplementedError("获取文件 URL 逻辑待实现")
    
    async def delete_file(self, object_name: str) -> None:
        """删除文件"""
        # TODO: 实现文件删除逻辑
        raise NotImplementedError("文件删除逻辑待实现")


# 全局存储客户端实例
storage_client: Optional[StorageClient] = None


def get_storage_client() -> StorageClient:
    """获取存储客户端实例"""
    global storage_client
    if storage_client is None:
        storage_client = StorageClient()
    return storage_client
