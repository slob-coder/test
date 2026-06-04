/**
 * M10: 任务状态模块 — 接口定义
 *
 * 覆盖功能: 统一异步任务状态查询、SSE 进度推送
 * 依赖: M01 (用户鉴权)
 */

import type {
  ProjectId,
  TaskId,
  AsyncTaskDTO,
  TaskProgressEvent,
  TaskCompletedEvent,
  TaskFailedEvent,
  ProjectStatusChangeEvent,
  PaginatedResponse,
} from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 查询任务列表请求 */
export interface ListTasksRequest {
  project_id?: ProjectId;    // 按项目筛选
  status?: AsyncTaskDTO['status'];  // 按状态筛选
  type?: AsyncTaskDTO['type'];      // 按任务类型筛选
  page?: number;
  page_size?: number;
}

/** 查询任务列表响应 */
export interface ListTasksResponse extends PaginatedResponse<AsyncTaskDTO> {}

/** 查询单个任务响应 */
export interface GetTaskResponse {
  task: AsyncTaskDTO;
}

/** SSE 连接端点响应（流式） */
export type TaskSSEStream =
  | TaskProgressEvent
  | TaskCompletedEvent
  | TaskFailedEvent
  | ProjectStatusChangeEvent;

// ============================================================
// API 端点契约
// ============================================================

/**
 * GET /api/v1/tasks
 *   查询当前用户的所有异步任务
 *   Query: ListTasksRequest
 *   Response: ListTasksResponse (200)
 *   错误: 401 — 未认证
 *
 * GET /api/v1/tasks/{task_id}
 *   查询单个任务详情
 *   Response: GetTaskResponse (200)
 *   错误: 401 — 未认证
 *         404 — 任务不存在
 *
 * GET /api/v1/tasks/{task_id}/stream
 *   SSE 实时推送任务进度
 *   Headers: Authorization: Bearer <token>
 *   Response: text/event-stream
 *   事件格式:
 *     event: task.progress
 *     data: TaskProgressEvent
 *
 *     event: task.completed
 *     data: TaskCompletedEvent
 *
 *     event: task.failed
 *     data: TaskFailedEvent
 *
 *     event: project.status_changed
 *     data: ProjectStatusChangeEvent
 *
 *   错误: 401 — 未认证
 *         404 — 任务不存在
 */
