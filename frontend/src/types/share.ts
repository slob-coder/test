/**
 * M09: 导出分享模块 — 接口定义
 *
 * 覆盖功能: F12 视频导出与分享
 * 依赖: M07 (合成视频产物)
 */

import type {
  CompositionId,
  ExportId,
  ShareId,
  ProjectId,
  Timestamp,
  ExportDTO,
  ShareLinkDTO,
} from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 视频导出请求 */
export interface ExportVideoRequest {
  composition_id: CompositionId;
  resolution: '720p' | '1080p';
}

/** 视频导出响应 */
export interface ExportVideoResponse {
  export: ExportDTO;
}

/** 分享链接生成请求 */
export interface CreateShareLinkRequest {
  composition_id: CompositionId;
  expires_in_days?: number;   // 有效期天数，默认 7
}

/** 分享链接生成响应 */
export interface CreateShareLinkResponse {
  share_link: ShareLinkDTO;
}

/** 获取分享视频响应（无需登录） */
export interface GetSharedVideoResponse {
  composition_id: CompositionId;
  project_name: string;
  video_url: string;
  resolution: string;
  duration: number;
  expires_at: Timestamp;
}

/** 获取项目导出列表响应 */
export interface ListExportsResponse {
  items: ExportDTO[];
  total: number;
}

/** 获取项目分享链接列表响应 */
export interface ListShareLinksResponse {
  items: ShareLinkDTO[];
  total: number;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * POST /api/v1/compositions/{composition_id}/export
 *   Request:  ExportVideoRequest
 *   Response: ExportVideoResponse (201)
 *   说明: 发起视频导出，返回导出记录
 *   错误: 404 — 合成任务不存在
 *         409 — 合成任务未完成，无法导出
 *
 * GET /api/v1/projects/{project_id}/exports
 *   Response: ListExportsResponse (200)
 *   说明: 获取项目的导出记录列表
 *
 * POST /api/v1/compositions/{composition_id}/share
 *   Request:  CreateShareLinkRequest
 *   Response: CreateShareLinkResponse (201)
 *   说明: 生成分享链接
 *   错误: 404 — 合成任务不存在
 *         409 — 合成任务未完成，无法分享
 *
 * GET /api/v1/projects/{project_id}/shares
 *   Response: ListShareLinksResponse (200)
 *   说明: 获取项目的分享链接列表
 *
 * GET /api/v1/share/{token}
 *   Response: GetSharedVideoResponse (200)
 *   说明: 访问分享视频（无需登录）
 *   错误: 404 — 分享链接不存在或已过期
 *
 * DELETE /api/v1/shares/{share_id}
 *   Response: { message: string } (200)
 *   说明: 撤销分享链接
 *   错误: 404 — 分享链接不存在
 */
