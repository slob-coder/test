/**
 * AI视频生成应用 — 全局共享类型定义
 *
 * 本文件定义前后端共享的核心数据结构，作为 API 契约的基础。
 * 后端 Python 实现应保持与这些类型的一一对应。
 *
 * ⚠️ 命名规范：所有字段使用 snake_case，与 API 规范一致。
 * ⚠️ 实时通信：统一使用 SSE，不使用 WebSocket。
 * ⚠️ API 路径前缀：统一使用 /api/v1/。
 */

// ============================================================
// ID 类型别名（增强可读性）
// ============================================================

export type UserId = string;
export type ProjectId = string;
export type ScriptId = string;
export type StoryboardId = string;
export type StoryboardItemId = string;
export type MediaId = string;
export type SubtitleId = string;
export type SubtitleEntryId = string;
export type CompositionId = string;
export type ExportId = string;
export type ShareId = string;
export type HistoryId = string;
export type TaskId = string;
export type Timestamp = string;  // ISO 8601

// ============================================================
// 通用类型
// ============================================================

/** 通用分页请求 */
export interface PaginationRequest {
  page: number;       // 页码，从 1 开始
  page_size: number;  // 每页条数，默认 20
}

/** 通用分页响应 */
export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

/** 通用 API 响应包装 */
export interface ApiResponse<T> {
  code: number;       // 业务状态码，0=成功
  message: string;    // 提示信息
  data: T;            // 业务数据
}

/** 排序方向 */
export type SortOrder = 'asc' | 'desc';

// ============================================================
// 用户模块 (M01-Auth)
// ============================================================

/** 用户注册请求 */
export interface RegisterRequest {
  username: string;   // 用户名，2-50字符，字母数字下划线
  password: string;   // 密码，≥6位
}

/** 用户登录请求 */
export interface LoginRequest {
  username: string;
  password: string;
}

/** 用户信息 DTO */
export interface UserDTO {
  id: UserId;
  username: string;
  created_at: Timestamp;
}

/** 登录响应（嵌套 UserDTO） */
export interface LoginResponse {
  access_token: string;   // JWT Token
  token_type: 'bearer';
  expires_in: number;     // 有效期（秒），默认 86400
  user: UserDTO;          // 嵌套用户信息
}

/** Token 刷新请求 */
export interface RefreshTokenRequest {
  refresh_token: string;
}

/** Token 刷新响应 */
export interface RefreshTokenResponse {
  access_token: string;
  token_type: 'bearer';
  expires_in: number;
}

// ============================================================
// 项目模块 (M02-Project)
// ============================================================

/** 项目创建请求 */
export interface CreateProjectRequest {
  name: string;         // 项目名称，必填 1-100字
  description?: string; // 项目描述，选填
}

/** 项目更新请求 */
export interface UpdateProjectRequest {
  name?: string;
  description?: string;
}

/**
 * 项目状态枚举
 * 采用过去分词表示"已完成某阶段"，failed 覆盖异常场景
 */
export type ProjectStatus =
  | 'draft'         // 草稿（刚创建）
  | 'scripted'      // 脚本完成
  | 'storyboarded'  // 分镜完成
  | 'materialized'  // 素材生成完成
  | 'compositing'   // 合成中
  | 'completed'     // 已完成
  | 'failed';       // 失败

/** 项目 DTO */
export interface ProjectDTO {
  id: ProjectId;
  name: string;
  description: string;
  status: ProjectStatus;
  user_id: UserId;
  thumbnail_url: string | null;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 项目列表项（轻量） */
export interface ProjectListItem {
  id: ProjectId;
  name: string;
  status: ProjectStatus;
  thumbnail_url: string | null;
  created_at: Timestamp;
  updated_at: Timestamp;
}

// ============================================================
// 脚本模块 (M03-Script)
// ============================================================

/** AI 生成脚本请求 */
export interface GenerateScriptRequest {
  project_id: ProjectId;
  topic: string;          // 视频主题，1-100字
  style?: string;         // 风格描述，如"纪录片风格"
  scene_count?: number;   // 期望场景数，默认 3-8
}

/** 上传脚本优化请求 */
export interface OptimizeScriptRequest {
  project_id: ProjectId;
  content: string;        // 原始脚本文本，≤5000字
  source: 'paste' | 'file';  // 来源方式
}

/** 脚本场景段落 */
export interface ScriptScene {
  id: string;             // 场景 UUID
  order: number;          // 场景序号
  scene_description: string;  // 场景描述
  narration: string;      // 旁白文本
  estimated_duration: number; // 预估时长（秒）
}

/** 脚本 DTO */
export interface ScriptDTO {
  id: ScriptId;
  project_id: ProjectId;
  scenes: ScriptScene[];
  source: 'ai_generated' | 'user_uploaded' | 'ai_optimized';
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 脚本保存请求 */
export interface SaveScriptRequest {
  project_id: ProjectId;
  scenes: ScriptScene[];
}

// ============================================================
// 分镜模块 (M04-Storyboard) — 两级结构：Storyboard + StoryboardItem
// ============================================================

/** 分镜容器 DTO */
export interface StoryboardDTO {
  id: StoryboardId;
  project_id: ProjectId;
  script_id: ScriptId;
  items: StoryboardItemDTO[];
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 分镜条目 DTO（对应分镜卡片/镜头） */
export interface StoryboardItemDTO {
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

/** 素材生成状态 */
export type AssetStatus =
  | 'pending'      // 待生成
  | 'generating'   // 生成中
  | 'completed'    // 已完成
  | 'failed';      // 生成失败

/** 分镜条目创建请求 */
export interface StoryboardItemCreate {
  order: number;
  scene_description: string;
  narration: string;
  estimated_duration?: number;
}

/** 分镜条目更新请求 */
export interface StoryboardItemUpdate {
  scene_description?: string;
  narration?: string;
  estimated_duration?: number;
}

// ============================================================
// 媒体生成模块 (M05-Media)
// ============================================================

/** 图片生成请求（单个分镜） */
export interface GenerateImageRequest {
  shot_id: StoryboardItemId;
  prompt?: string;       // 可选自定义提示词，默认使用 scene_description
}

/** 批量图片生成请求 */
export interface BatchGenerateImagesRequest {
  project_id: ProjectId;
  shot_ids?: StoryboardItemId[];   // 为空则生成所有 pending 的分镜
}

/** 视频片段生成请求 */
export interface GenerateVideoClipRequest {
  shot_id: StoryboardItemId;
  duration?: number;     // 视频时长，默认 3-5 秒
}

/** 批量视频片段生成请求 */
export interface BatchGenerateVideoClipsRequest {
  project_id: ProjectId;
  shot_ids?: StoryboardItemId[];
}

/** 媒体文件 DTO */
export interface MediaDTO {
  id: MediaId;
  storyboard_item_id: StoryboardItemId;
  media_type: 'image' | 'video';
  file_url: string;          // 访问 URL
  file_size: number;         // 文件大小（字节）
  width: number | null;
  height: number | null;
  duration: number | null;   // 视频时长（秒）
  source: 'ai_generated' | 'user_uploaded';
  created_at: Timestamp;
}

// ============================================================
// 字幕模块 (M06-Subtitle)
// ============================================================

/** 字幕条目（统一结构，snake_case） */
export interface SubtitleEntry {
  id: SubtitleEntryId;
  subtitle_id: SubtitleId;               // 所属字幕容器 ID
  project_id: ProjectId;
  storyboard_item_id: StoryboardItemId;  // 关联分镜条目 ID
  index: number;              // 字幕序号
  start_time: number;         // 起始时间（秒，精确到毫秒）
  end_time: number;           // 结束时间（秒，精确到毫秒）
  text: string;               // 字幕文本
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 字幕容器 DTO（一个项目对应一组字幕） */
export interface SubtitleDTO {
  id: SubtitleId;
  project_id: ProjectId;
  entries: SubtitleEntry[];
  format: 'srt';
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 字幕条目更新请求 */
export interface SubtitleEntryUpdate {
  id: SubtitleEntryId;
  text?: string;
  start_time?: number;
  end_time?: number;
}

/** SRT 条目（导出格式） */
export interface SRTEntry {
  index: number;
  start_time: string;          // HH:MM:SS,mmm
  end_time: string;            // HH:MM:SS,mmm
  text: string;
}

// ============================================================
// 视频合成模块 (M07-Composition)
// ============================================================

/** 视频合成请求 */
export interface ComposeVideoRequest {
  project_id: ProjectId;
  resolution?: '720p' | '1080p';  // 默认 720p
  fps?: 24 | 30;                   // 帧率，默认 24
  use_video_clips?: boolean;       // 是否使用视频片段（而非静态图片），默认 false
  include_subtitles?: boolean;     // 是否包含字幕，默认 true
}

/** 合成任务状态 */
export type CompositionTaskStatus =
  | 'pending'
  | 'processing'
  | 'completed'
  | 'failed';

/** 合成任务 DTO */
export interface ComposeTaskDTO {
  id: CompositionId;
  project_id: ProjectId;
  status: CompositionTaskStatus;
  progress: number;       // 0-100
  current_step: string;   // 当前步骤描述
  resolution: string;
  fps: number;
  output_url: string | null;
  error_message: string | null;
  created_at: Timestamp;
  completed_at: Timestamp | null;
}

/** 视频产物 DTO */
export interface VideoProductDTO {
  id: string;
  project_id: ProjectId;
  url: string;            // 视频文件 URL
  resolution: string;
  duration: number;       // 视频时长（秒）
  file_size: number;      // 文件大小（字节）
  format: 'mp4';
  created_at: Timestamp;
}

// ============================================================
// 历史记录模块 (M08-History)
// ============================================================

/** 操作类型枚举 */
export type HistoryActionType =
  | 'script_generated'
  | 'script_modified'
  | 'script_optimized'
  | 'storyboard_split'
  | 'shot_modified'
  | 'shot_reordered'
  | 'shot_added'
  | 'shot_deleted'
  | 'image_generated'
  | 'video_clip_generated'
  | 'subtitle_generated'
  | 'subtitle_modified'
  | 'video_composed'
  | 'video_exported';

/** 历史记录条目 */
export interface HistoryEntryDTO {
  id: HistoryId;
  project_id: ProjectId;
  action_type: HistoryActionType;
  summary: string;          // 操作摘要
  detail: Record<string, unknown> | null;  // 操作详情（JSON）
  created_at: Timestamp;
}

// ============================================================
// 导出分享模块 (M09-Share)
// ============================================================

/** 视频导出请求 */
export interface ExportVideoRequest {
  project_id: ProjectId;
  composition_id: CompositionId;
  resolution: '720p' | '1080p';
}

/** 导出记录 DTO */
export interface ExportDTO {
  id: ExportId;
  composition_id: CompositionId;
  resolution: string;
  file_url: string;
  file_size: number;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  created_at: Timestamp;
}

/** 分享链接生成请求 */
export interface CreateShareLinkRequest {
  composition_id: CompositionId;
  expires_in_days?: number;  // 有效期天数，默认 7
}

/** 分享链接 DTO */
export interface ShareLinkDTO {
  id: ShareId;
  url: string;              // 分享链接
  composition_id: CompositionId;
  expires_at: Timestamp;
  created_at: Timestamp;
}

// ============================================================
// 任务状态模块 (M10-Task) — SSE 事件
// ============================================================

/** 异步任务 DTO */
export interface AsyncTaskDTO {
  id: TaskId;
  type: 'script_generation' | 'image_generation' | 'video_clip_generation' | 'video_composition' | 'video_export';
  status: 'queued' | 'processing' | 'completed' | 'failed';
  project_id: ProjectId;
  progress: number;       // 0-100
  error_message: string | null;
  created_at: Timestamp;
  completed_at: Timestamp | null;
}

// ============================================================
// SSE 事件类型（统一实时通信方案）
// ============================================================

/** SSE 事件类型枚举 */
export type SSEEventType =
  | 'task_progress'
  | 'task_completed'
  | 'task_failed'
  | 'project_status_changed';

/** SSE 事件基础结构 */
export interface SSEEvent<T = unknown> {
  event_type: SSEEventType;
  task_id?: TaskId;
  project_id?: ProjectId;
  data: T;
}

/** AI 任务进度事件（SSE） */
export interface TaskProgressEvent {
  task_id: TaskId;
  task_type: 'script_generation' | 'image_generation' | 'video_clip_generation' | 'video_composition' | 'video_export';
  shot_id: StoryboardItemId | null;
  status: 'queued' | 'processing' | 'completed' | 'failed';
  progress: number;       // 0-100
  current_step: string;
  error_message: string | null;
}

/** 任务完成事件（SSE） */
export interface TaskCompletedEvent {
  task_id: TaskId;
  task_type: string;
  result: Record<string, unknown>;
}

/** 任务失败事件（SSE） */
export interface TaskFailedEvent {
  task_id: TaskId;
  task_type: string;
  error: string;
}

/** 项目状态变更事件（SSE） */
export interface ProjectStatusChangeEvent {
  project_id: ProjectId;
  old_status: ProjectStatus;
  new_status: ProjectStatus;
}
