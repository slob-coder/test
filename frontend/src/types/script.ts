/**
 * M03: 脚本生成模块 — 接口定义
 *
 * 覆盖功能: F03 AI自动生成脚本, F04 用户上传脚本优化
 * 依赖: M02 (项目上下文)
 */

import type { ProjectId, ScriptId, Timestamp } from './types';

// ============================================================
// 请求类型
// ============================================================

/** AI 生成脚本请求 */
export interface GenerateScriptRequest {
  project_id: ProjectId;
  topic: string;              // 视频主题，1-100字
  style?: string;             // 风格描述，如"纪录片风格"
  scene_count?: number;       // 期望场景数，默认3-8
}

/** 上传脚本优化请求 */
export interface OptimizeScriptRequest {
  project_id: ProjectId;
  content: string;            // 脚本文本内容，≤5000字
  source: 'paste' | 'file';  // 来源方式
}

/** 保存脚本请求 */
export interface SaveScriptRequest {
  project_id: ProjectId;
  scenes: SceneCreate[];
}

/** 单个场景创建/更新 */
export interface SceneCreate {
  id?: string;                // 更新时传入
  scene_description: string;
  narration: string;
  order: number;
}

// ============================================================
// 响应类型
// ============================================================

/** 脚本生成响应 */
export interface GenerateScriptResponse {
  script_id: ScriptId;
  scenes: GeneratedScene[];
  model_used: string;         // 使用的AI模型标识
  generated_at: Timestamp;
}

/** 脚本优化响应 */
export interface OptimizeScriptResponse {
  original_content: string;
  optimized_scenes: GeneratedScene[];
  changes_summary: string;    // 优化摘要说明
}

/** 脚本保存响应 */
export interface SaveScriptResponse {
  script_id: ScriptId;
  scene_count: number;
  saved_at: Timestamp;
}

/** 生成的场景 */
export interface GeneratedScene {
  order: number;
  scene_description: string;
  narration: string;
  estimated_duration: number;  // 预估时长(秒)
}

// ============================================================
// API 路由契约
// ============================================================

/**
 * POST   /api/v1/scripts/generate          → GenerateScriptResponse
 * POST   /api/v1/scripts/optimize          → OptimizeScriptResponse
 * PUT    /api/v1/scripts/{project_id}      → SaveScriptResponse
 * GET    /api/v1/scripts/{project_id}      → ScriptDetail
 */
