/**
 * M01: 用户认证模块 — 接口定义
 *
 * 覆盖功能: F01 用户注册与登录
 * 依赖: 无
 *
 * 统一约定:
 * - API 路径前缀: /api/v1/
 * - 字段命名: snake_case
 */

import type { UserId, Timestamp, UserDTO } from './types';

// ============================================================
// 请求 / 响应类型
// ============================================================

/** 用户注册请求 */
export interface RegisterRequest {
  username: string;   // 2-50字符，字母数字下划线
  password: string;   // ≥6字符
}

/** 用户注册响应 */
export interface RegisterResponse {
  user_id: UserId;
  username: string;
}

/** 用户登录请求 */
export interface LoginRequest {
  username: string;
  password: string;
}

/** 用户登录响应 — 嵌套 UserDTO */
export interface LoginResponse {
  access_token: string;   // JWT Token
  token_type: 'bearer';
  expires_in: number;     // 秒，86400
  user: UserDTO;          // 嵌套用户信息
}

/** Token 刷新请求 */
export interface RefreshTokenRequest {
  access_token: string;   // 当前 Token（仍有效期内或宽限期内）
}

/** Token 刷新响应 */
export interface RefreshTokenResponse {
  access_token: string;
  token_type: 'bearer';
  expires_in: number;
}

/** 当前用户信息响应 */
export interface MeResponse extends UserDTO {}

// ============================================================
// API 端点
// ============================================================

/**
 * POST /api/v1/auth/register
 * 请求体: RegisterRequest
 * 响应:   RegisterResponse (201)
 * 错误:   409 — 用户名已存在
 *         422 — 参数校验失败
 */

/**
 * POST /api/v1/auth/login
 * 请求体: LoginRequest
 * 响应:   LoginResponse (200)
 * 错误:   401 — 用户名或密码错误
 *         422 — 参数校验失败
 */

/**
 * POST /api/v1/auth/refresh
 * 请求体: RefreshTokenRequest
 * 响应:   RefreshTokenResponse (200)
 * 错误:   401 — Token 无效或已过期
 */

/**
 * GET /api/v1/auth/me
 * Headers: Authorization: Bearer <token>
 * 响应:   MeResponse (200)
 * 错误:   401 — 未认证 / Token 过期
 */
