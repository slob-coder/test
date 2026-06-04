/**
 * 视频合成模块接口定义 (M07: Composition)
 *
 * 覆盖功能: F10 视频合成
 * 依赖: M04 (分镜数据), M05 (媒体素材), M06 (字幕数据)
 *
 * 统一约定：
 * - API 路径前缀: /api/v1/
 * - 实时通信: SSE (Server-Sent Events)
 * - 字段命名: snake_case
 */

import type {
  ProjectId,
  CompositionId,
  CompositionTaskStatus,
  ComposeTaskDTO,
  VideoProductDTO,
  Timestamp,
} from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 发起视频合成请求 */
export interface ComposeVideoRequest {
  project_id: ProjectId;
  /** 合成设置 */
  settings: CompositionSettings;
}

/** 合成设置 */
export interface CompositionSettings {
  /** 输出分辨率 */
  resolution: '720p' | '1080p';
  /** 帧率 */
  fps: 24 | 30;
  /** 是否使用视频片段（而非静态图片），默认 false */
  use_video_clips?: boolean;
  /** 是否包含字幕 */
  include_subtitles: boolean;
  /** 字幕样式 */
  subtitle_style?: SubtitleStyle;
}

/** 字幕样式 */
export interface SubtitleStyle {
  font_size: number;       // 字号，默认 24
  font_color: string;      // 颜色，默认 "#FFFFFF"
  outline_color: string;   // 描边颜色，默认 "#000000"
  outline_width: number;   // 描边宽度，默认 2
  position: 'bottom' | 'top' | 'middle'; // 位置
}

/** 合成任务响应 */
export interface ComposeVideoResponse {
  task_id: string;
  project_id: ProjectId;
  status: CompositionTaskStatus;
  /** 预估完成时间（秒） */
  estimated_duration: number;
}

/** 合成任务详情 */
export interface CompositionTask {
  task_id: string;
  project_id: ProjectId;
  settings: CompositionSettings;
  status: CompositionTaskStatus;
  progress: number; // 0-100
  /** 已完成的步骤描述 */
  current_step: string;
  /** 合成结果（仅 completed 状态） */
  result?: CompositionResult;
  /** 错误信息（仅 failed 状态） */
  error?: string;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 合成结果 */
export interface CompositionResult {
  /** 视频文件 URL */
  video_url: string;
  /** 文件大小（字节） */
  file_size: number;
  /** 视频时长（秒） */
  duration: number;
  /** 分辨率 */
  resolution: string;
  /** 帧率 */
  fps: number;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * POST /api/v1/projects/{project_id}/compose
 *   Request:  ComposeVideoRequest
 *   Response: ComposeVideoResponse
 *   说明: 发起视频合成，返回异步任务 ID
 *
 * GET /api/v1/compositions/{task_id}
 *   Response: CompositionTask
 *   说明: 查询合成任务状态和进度
 *
 * GET /api/v1/projects/{project_id}/compositions
 *   Response: { items: CompositionTask[] }
 *   说明: 获取项目的合成历史
 *
 * POST /api/v1/compositions/{task_id}/cancel
 *   Response: { success: boolean }
 *   说明: 取消进行中的合成任务
 */

// ============================================================
// SSE 事件定义（统一实时通信方案）
// ============================================================

/** 合成完成 SSE 事件 */
export interface CompositionCompletedEvent {
  event_type: 'composition.completed';
  task_id: string;
  project_id: ProjectId;
  result: CompositionResult;
}

/** 合成进度 SSE 事件 */
export interface CompositionProgressEvent {
  event_type: 'composition.progress';
  task_id: string;
  project_id: ProjectId;
  progress: number;
  current_step: string;
}

/** 合成失败 SSE 事件 */
export interface CompositionFailedEvent {
  event_type: 'composition.failed';
  task_id: string;
  project_id: ProjectId;
  error: string;
}
