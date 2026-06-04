/**
 * M05: 媒体生成模块 — 接口定义
 *
 * 覆盖功能: F06 AI生成分镜图片, F07 AI生成分镜视频片段
 * 依赖: M04 (分镜数据), Celery (异步任务), AI-图片/视频服务, MinIO (文件存储)
 */

import type {
  ProjectId,
  StoryboardItemId,
  MediaId,
  MediaDTO,
  AssetStatus,
  Timestamp,
} from './types';

// ============================================================
// 请求类型
// ============================================================

/** 生成单个分镜图片请求 */
export interface GenerateImageRequest {
  shot_id: StoryboardItemId;
  prompt?: string;           // 可选自定义提示词，默认使用 scene_description
}

/** 批量生成图片请求 */
export interface BatchGenerateImagesRequest {
  project_id: ProjectId;
  shot_ids?: StoryboardItemId[];  // 为空则生成所有 pending 的分镜
}

/** 生成单个视频片段请求 */
export interface GenerateVideoClipRequest {
  shot_id: StoryboardItemId;
  duration?: number;         // 视频时长，默认 3-5 秒
}

/** 批量生成视频片段请求 */
export interface BatchGenerateVideoClipsRequest {
  project_id: ProjectId;
  shot_ids?: StoryboardItemId[];
}

/** 上传替换图片请求（multipart/form-data） */
export interface UploadImageRequest {
  /** 上传的图片文件（.jpg/.png，≤5MB） */
  file: File;
}

// ============================================================
// 响应类型
// ============================================================

/** 单个图片生成响应 */
export interface GenerateImageResponse {
  task_id: string;
  shot_id: StoryboardItemId;
  status: AssetStatus;
  message: string;           // 如"图片生成任务已提交"
}

/** 批量图片生成响应 */
export interface BatchGenerateImagesResponse {
  task_id: string;
  project_id: ProjectId;
  total_count: number;       // 总共需要生成的数量
  submitted_count: number;   // 已提交生成的数量
  message: string;
}

/** 单个视频片段生成响应 */
export interface GenerateVideoClipResponse {
  task_id: string;
  shot_id: StoryboardItemId;
  status: AssetStatus;
  message: string;
}

/** 批量视频片段生成响应 */
export interface BatchGenerateVideoClipsResponse {
  task_id: string;
  project_id: ProjectId;
  total_count: number;
  submitted_count: number;
  message: string;
}

/** 上传图片响应 */
export interface UploadImageResponse {
  media: MediaDTO;
  shot_id: StoryboardItemId;
  message: string;
}

/** 获取媒体文件详情响应 */
export interface GetMediaResponse {
  media: MediaDTO;
}

/** 获取项目所有媒体文件响应 */
export interface ListProjectMediaResponse {
  items: MediaDTO[];
  total: number;
}

// ============================================================
// SSE 事件类型
// ============================================================

/** 图片生成进度 SSE 事件 */
export interface ImageGenerationProgressEvent {
  shot_id: StoryboardItemId;
  progress: number;          // 0-100
  message: string;           // 如"正在生成分镜 3 的图片..."
}

/** 图片生成完成 SSE 事件 */
export interface ImageGenerationCompletedEvent {
  shot_id: StoryboardItemId;
  media: MediaDTO;
}

/** 视频片段生成进度 SSE 事件 */
export interface VideoClipGenerationProgressEvent {
  shot_id: StoryboardItemId;
  progress: number;
  message: string;
}

/** 视频片段生成完成 SSE 事件 */
export interface VideoClipGenerationCompletedEvent {
  shot_id: StoryboardItemId;
  media: MediaDTO;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * POST /api/v1/storyboard-items/{shot_id}/generate-image
 *   Request:  GenerateImageRequest
 *   Response: GenerateImageResponse (202)
 *   说明: 提交单个分镜的图片生成任务
 *
 * POST /api/v1/projects/{project_id}/generate-images
 *   Request:  BatchGenerateImagesRequest
 *   Response: BatchGenerateImagesResponse (202)
 *   说明: 批量提交图片生成任务
 *
 * POST /api/v1/storyboard-items/{shot_id}/generate-video
 *   Request:  GenerateVideoClipRequest
 *   Response: GenerateVideoClipResponse (202)
 *   说明: 提交单个分镜的视频片段生成任务
 *
 * POST /api/v1/projects/{project_id}/generate-videos
 *   Request:  BatchGenerateVideoClipsRequest
 *   Response: BatchGenerateVideoClipsResponse (202)
 *   说明: 批量提交视频片段生成任务
 *
 * POST /api/v1/storyboard-items/{shot_id}/upload-image
 *   Request:  UploadImageRequest (multipart/form-data)
 *   Response: UploadImageResponse (200)
 *   说明: 上传图片替换 AI 生成的图片
 *   错误:   413 — 文件过大
 *           415 — 不支持的文件类型
 *
 * GET /api/v1/media/{media_id}
 *   Response: GetMediaResponse (200)
 *   说明: 获取媒体文件详情
 *
 * GET /api/v1/projects/{project_id}/media
 *   Response: ListProjectMediaResponse (200)
 *   说明: 获取项目所有媒体文件
 *
 * 错误:
 *   401 — 未认证
 *   403 — 无权限
 *   404 — 分镜/项目不存在
 *   422 — 参数校验失败
 */
