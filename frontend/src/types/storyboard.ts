/**
 * M04: 分镜管理模块 — 接口定义
 *
 * 覆盖功能: F05 脚本自动拆分分镜, F08 分镜手动调整
 * 依赖: M03 (脚本数据)
 *
 * 数据模型: 两级结构（Storyboard 容器 + StoryboardItem 条目）
 */

import type {
  StoryboardId,
  StoryboardItemId,
  ProjectId,
  ScriptId,
  Timestamp,
  AssetStatus,
  StoryboardItemCreate,
  StoryboardItemUpdate,
} from './types';

// ============================================================
// 数据模型（与 types.ts 中的 StoryboardDTO / StoryboardItemDTO 对齐）
// ============================================================

/** 分镜容器（一个项目对应一个分镜容器） */
export interface Storyboard {
  id: StoryboardId;
  project_id: ProjectId;
  script_id: ScriptId;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 分镜条目（每个条目对应一个镜头） */
export interface StoryboardItem {
  id: StoryboardItemId;
  storyboard_id: StoryboardId;
  order: number;              // 序号
  scene_description: string;  // 场景描述
  narration: string;          // 旁白文本
  estimated_duration: number; // 预估时长（秒）
  image_url: string | null;   // 分镜图片 URL
  video_url: string | null;   // 分镜视频 URL
  image_status: AssetStatus;  // 图片生成状态
  video_status: AssetStatus;  // 视频生成状态
}

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 从脚本生成分镜请求 */
export interface GenerateStoryboardRequest {
  script_id: ScriptId;
}

/** 从脚本生成分镜响应 */
export interface GenerateStoryboardResponse {
  storyboard: Storyboard;
  items: StoryboardItem[];
}

/** 获取分镜列表响应 */
export interface GetStoryboardResponse {
  storyboard: Storyboard;
  items: StoryboardItem[];
}

/** 调整分镜顺序请求 */
export interface ReorderStoryboardRequest {
  /** 有序的分镜项ID列表 */
  item_ids: StoryboardItemId[];
}

/** 调整分镜顺序响应 */
export interface ReorderStoryboardResponse {
  items: StoryboardItem[];
}

/** 新增分镜项请求 */
export interface CreateStoryboardItemRequest extends StoryboardItemCreate {}

/** 新增分镜项响应 */
export interface CreateStoryboardItemResponse {
  item: StoryboardItem;
}

/** 更新分镜项请求 */
export interface UpdateStoryboardItemRequest extends StoryboardItemUpdate {}

/** 更新分镜项响应 */
export interface UpdateStoryboardItemResponse {
  item: StoryboardItem;
}

/** 删除分镜项响应 */
export interface DeleteStoryboardItemResponse {
  message: string;
}

/** 拆分分镜请求 */
export interface SplitStoryboardItemRequest {
  /** 拆分位置（旁白文本中的字符偏移量） */
  split_offset: number;
}

/** 拆分分镜响应 */
export interface SplitStoryboardItemResponse {
  item_a: StoryboardItem;
  item_b: StoryboardItem;
}

/** 合并分镜请求 */
export interface MergeStoryboardItemsRequest {
  /** 要合并的分镜项ID列表（必须相邻） */
  item_ids: [StoryboardItemId, StoryboardItemId];
}

/** 合并分镜响应 */
export interface MergeStoryboardItemsResponse {
  merged_item: StoryboardItem;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * GET    /api/v1/projects/{project_id}/storyboard              → GetStoryboardResponse (200)
 * POST   /api/v1/projects/{project_id}/storyboard/generate     → GenerateStoryboardResponse (201)
 * PUT    /api/v1/projects/{project_id}/storyboard/reorder      → ReorderStoryboardResponse (200)
 * POST   /api/v1/projects/{project_id}/storyboard/items        → CreateStoryboardItemResponse (201)
 * PUT    /api/v1/storyboard-items/{item_id}                    → UpdateStoryboardItemResponse (200)
 * DELETE /api/v1/storyboard-items/{item_id}                    → DeleteStoryboardItemResponse (200)
 * POST   /api/v1/storyboard-items/{item_id}/split              → SplitStoryboardItemResponse (200)
 * POST   /api/v1/storyboard-items/merge                        → MergeStoryboardItemsResponse (200)
 *
 * 错误:
 *   401 — 未认证
 *   403 — 无权限（非本人项目）
 *   404 — 项目/分镜不存在
 *   422 — 参数校验失败
 */
