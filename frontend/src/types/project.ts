/**
 * M02: 项目管理模块 — 接口定义
 *
 * 覆盖功能: F02 项目管理
 * 依赖: M01 (用户鉴权)
 */

import type { ProjectId, ProjectStatus, Timestamp } from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 创建项目请求 */
export interface CreateProjectRequest {
  name: string;           // 项目名称（必填，1-100字）
  description?: string;   // 项目描述（选填）
}

/** 创建项目响应 */
export interface CreateProjectResponse {
  id: ProjectId;
  name: string;
  description: string;
  status: ProjectStatus;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 获取项目列表请求 */
export interface ListProjectsRequest {
  page?: number;          // 页码，默认1
  page_size?: number;     // 每页数量，默认20
  status?: ProjectStatus; // 按状态筛选
}

/** 项目列表项 */
export interface ProjectListItem {
  id: ProjectId;
  name: string;
  status: ProjectStatus;
  thumbnail_url: string | null;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 获取项目列表响应 */
export interface ListProjectsResponse {
  items: ProjectListItem[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

/** 获取项目详情响应 */
export interface GetProjectResponse {
  id: ProjectId;
  name: string;
  description: string;
  status: ProjectStatus;
  user_id: string;
  thumbnail_url: string | null;
  created_at: Timestamp;
  updated_at: Timestamp;
}

/** 更新项目请求 */
export interface UpdateProjectRequest {
  name?: string;
  description?: string;
}

/** 更新项目响应 */
export interface UpdateProjectResponse {
  id: ProjectId;
  name: string;
  description: string;
  status: ProjectStatus;
  updated_at: Timestamp;
}

/** 删除项目响应 */
export interface DeleteProjectResponse {
  message: string;
}

// ============================================================
// API 端点契约
// ============================================================

/**
 * POST   /api/v1/projects              → CreateProjectResponse (201)
 * GET    /api/v1/projects              → ListProjectsResponse (200)
 * GET    /api/v1/projects/{project_id} → GetProjectResponse (200)
 * PUT    /api/v1/projects/{project_id} → UpdateProjectResponse (200)
 * DELETE /api/v1/projects/{project_id} → DeleteProjectResponse (200)
 *
 * 错误:
 *   401 — 未认证
 *   403 — 无权限（非本人项目）
 *   404 — 项目不存在
 *   422 — 参数校验失败
 */
