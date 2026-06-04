/**
 * M02: 项目管理 API
 */

import client from './client';
import type {
  CreateProjectRequest,
  CreateProjectResponse,
  ListProjectsRequest,
  ListProjectsResponse,
  GetProjectResponse,
  UpdateProjectRequest,
  UpdateProjectResponse,
} from '../types/project';

export const projectApi = {
  /**
   * 创建项目
   * POST /api/v1/projects
   */
  create: async (data: CreateProjectRequest): Promise<CreateProjectResponse> => {
    return client.post('/projects', data);
  },

  /**
   * 获取项目列表
   * GET /api/v1/projects
   */
  list: async (params?: ListProjectsRequest): Promise<ListProjectsResponse> => {
    return client.get('/projects', { params });
  },

  /**
   * 获取项目详情
   * GET /api/v1/projects/{project_id}
   */
  get: async (projectId: string): Promise<GetProjectResponse> => {
    return client.get(`/projects/${projectId}`);
  },

  /**
   * 更新项目
   * PUT /api/v1/projects/{project_id}
   */
  update: async (projectId: string, data: UpdateProjectRequest): Promise<UpdateProjectResponse> => {
    return client.put(`/projects/${projectId}`, data);
  },

  /**
   * 删除项目
   * DELETE /api/v1/projects/{project_id}
   */
  delete: async (projectId: string): Promise<{ message: string }> => {
    return client.delete(`/projects/${projectId}`);
  },
};

export default projectApi;
