/**
 * M08: 历史记录模块 — 接口定义
 *
 * 覆盖功能: F11 历史记录管理
 * 依赖: M02 (项目上下文)
 */

import type {
  ProjectId,
  HistoryId,
  HistoryActionType,
  HistoryEntryDTO,
  PaginatedResponse,
  Timestamp,
} from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 获取历史记录列表请求 */
export interface ListHistoryRequest {
  page?: number;              // 页码，默认1
  page_size?: number;         // 每页数量，默认20
  action_type?: HistoryActionType;  // 按操作类型筛选
  start_date?: Timestamp;     // 起始日期筛选
  end_date?: Timestamp;       // 结束日期筛选
}

/** 获取历史记录列表响应 */
export interface ListHistoryResponse extends PaginatedResponse<HistoryEntryDTO> {}

/** 获取历史详情响应 */
export interface GetHistoryDetailResponse {
  id: HistoryId;
  project_id: ProjectId;
  action_type: HistoryActionType;
  summary: string;
  detail: Record<string, unknown> | null;
  snapshot_before: Record<string, unknown> | null;  // 操作前快照
  snapshot_after: Record<string, unknown> | null;   // 操作后快照
  created_at: Timestamp;
}

/** 回滚请求（可选功能） */
export interface RollbackRequest {
  history_id: HistoryId;
  confirm: boolean;           // 必须为 true 才执行回滚
}

/** 回滚响应 */
export interface RollbackResponse {
  success: boolean;
  message: string;
  restored_project_status: string;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * GET /api/v1/projects/{project_id}/histories
 *   Request:  ListHistoryRequest (query params)
 *   Response: ListHistoryResponse (200)
 *   说明: 获取项目操作历史记录（分页）
 *   错误:
 *     401 — 未认证
 *     403 — 无权限
 *     404 — 项目不存在
 *
 * GET /api/v1/histories/{history_id}
 *   Response: GetHistoryDetailResponse (200)
 *   说明: 获取单条历史记录详情（含快照）
 *   错误:
 *     401 — 未认证
 *     404 — 历史记录不存在
 *
 * POST /api/v1/histories/{history_id}/rollback
 *   Request:  RollbackRequest
 *   Response: RollbackResponse (200)
 *   说明: 回滚到指定历史版本（可选功能）
 *   错误:
 *     401 — 未认证
 *     403 — 无权限
 *     404 — 历史记录不存在
 *     409 — 回滚冲突（当前状态不允许回滚）
 */
