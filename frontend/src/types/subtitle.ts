/**
 * M06: 字幕生成模块 — 接口定义
 *
 * 覆盖功能: F09 字幕自动生成
 * 依赖: M04 (分镜数据)
 *
 * 统一约定:
 * - API 路径前缀: /api/v1/
 * - 字段命名: snake_case
 * - 实时通信: SSE
 */

import type { SubtitleId, ProjectId, StoryboardItemId, Timestamp } from './types';

// ============================================================
// 数据模型
// ============================================================

/** 字幕条目（统一结构，snake_case） */
export interface SubtitleEntry {
  id: SubtitleId;
  project_id: ProjectId;
  storyboard_item_id: StoryboardItemId;  // 关联分镜条目 ID
  index: number;              // 字幕序号
  start_time: number;         // 起始时间（秒，精确到毫秒）
  end_time: number;           // 结束时间（秒，精确到毫秒）
  text: string;               // 字幕文本
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** SRT 格式条目（导出格式） */
export interface SRTEntry {
  index: number;
  start_time: string;          // HH:MM:SS,mmm
  end_time: string;            // HH:MM:SS,mmm
  text: string;
}

// ============================================================
// 请求类型
// ============================================================

/** 字幕自动生成请求 */
export interface GenerateSubtitlesRequest {
  storyboard_item_ids?: StoryboardItemId[];  // 指定分镜条目，为空则根据全部生成
}

/** 字幕条目更新请求 */
export interface UpdateSubtitleRequest {
  text?: string;
  start_time?: number;
  end_time?: number;
}

// ============================================================
// 响应类型
// ============================================================

/** 字幕生成响应 */
export interface GenerateSubtitlesResponse {
  subtitles: SubtitleEntry[];
  total_count: number;
}

/** 字幕列表响应 */
export interface ListSubtitlesResponse {
  subtitles: SubtitleEntry[];
  total_count: number;
}

/** 字幕更新响应 */
export interface UpdateSubtitleResponse {
  subtitle: SubtitleEntry;
}

/** 字幕导出响应 */
export interface ExportSubtitlesResponse {
  content: string;            // SRT 格式文本
  format: 'srt';
}

/** 字幕删除响应 */
export interface DeleteSubtitlesResponse {
  deleted_count: number;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * POST   /api/v1/projects/{project_id}/subtitles/generate
 *   Request:  GenerateSubtitlesRequest
 *   Response: GenerateSubtitlesResponse (200)
 *   说明: 从分镜旁白自动生成字幕
 *   错误: 401 / 403 / 404 / 422
 */

/**
 * GET    /api/v1/projects/{project_id}/subtitles
 *   Response: ListSubtitlesResponse (200)
 *   说明: 获取项目字幕列表
 *   错误: 401 / 403 / 404
 */

/**
 * PUT    /api/v1/subtitles/{subtitle_id}
 *   Request:  UpdateSubtitleRequest
 *   Response: UpdateSubtitleResponse (200)
 *   说明: 更新字幕条目
 *   错误: 401 / 403 / 404 / 422
 */

/**
 * GET    /api/v1/projects/{project_id}/subtitles/export-srt
 *   Response: ExportSubtitlesResponse (200)
 *   说明: 导出字幕（SRT 格式）
 *   错误: 401 / 403 / 404
 */

/**
 * DELETE /api/v1/projects/{project_id}/subtitles
 *   Response: DeleteSubtitlesResponse (200)
 *   说明: 删除项目全部字幕（重新生成前清除）
 *   错误: 401 / 403 / 404
 */
