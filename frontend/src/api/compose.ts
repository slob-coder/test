/**
 * M07: 视频合成 API
 */

import client from './client';
import type {
  ComposeVideoRequest,
  ComposeVideoResponse,
  GetCompositionResponse,
  ListCompositionsResponse,
} from '../types/composition';

export const composeApi = {
  /**
   * 发起视频合成
   * POST /api/v1/projects/{project_id}/compose
   */
  compose: async (projectId: string, data?: ComposeVideoRequest): Promise<ComposeVideoResponse> => {
    return client.post(`/projects/${projectId}/compose`, data);
  },

  /**
   * 查询合成任务状态
   * GET /api/v1/compositions/{task_id}
   */
  getStatus: async (taskId: string): Promise<GetCompositionResponse> => {
    return client.get(`/compositions/${taskId}`);
  },

  /**
   * 获取合成历史
   * GET /api/v1/projects/{project_id}/compositions
   */
  list: async (projectId: string): Promise<ListCompositionsResponse> => {
    return client.get(`/projects/${projectId}/compositions`);
  },

  /**
   * 取消合成任务
   * POST /api/v1/compositions/{task_id}/cancel
   */
  cancel: async (taskId: string): Promise<void> => {
    return client.post(`/compositions/${taskId}/cancel`);
  },
};

export default composeApi;
