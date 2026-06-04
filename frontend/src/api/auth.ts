/**
 * M01: 认证 API
 */

import client from './client';
import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
  RefreshTokenResponse,
  MeResponse,
} from '../types/auth';

export const authApi = {
  /**
   * 用户登录
   * POST /api/v1/auth/login
   */
  login: async (data: LoginRequest): Promise<LoginResponse> => {
    return client.post('/auth/login', data);
  },

  /**
   * 用户注册
   * POST /api/v1/auth/register
   */
  register: async (data: RegisterRequest): Promise<RegisterResponse> => {
    return client.post('/auth/register', data);
  },

  /**
   * 刷新 Token
   * POST /api/v1/auth/refresh
   */
  refreshToken: async (): Promise<RefreshTokenResponse> => {
    const token = localStorage.getItem('access_token');
    return client.post('/auth/refresh', { access_token: token });
  },

  /**
   * 获取当前用户信息
   * GET /api/v1/auth/me
   */
  getMe: async (): Promise<MeResponse> => {
    return client.get('/auth/me');
  },
};

export default authApi;
