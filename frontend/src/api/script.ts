/**
 * M03: 脚本生成 API
 */

import client from './client';
import type {
  GenerateScriptRequest,
  GenerateScriptResponse,
  GetScriptResponse,
  UpdateScriptRequest,
  UpdateScriptResponse,
} from '../types/script';

export const scriptApi = {
  /**
   * AI 生成脚本
   * POST /api/v1/scripts/{project_id}/generate
   */
  generate: async (projectId: string, data: GenerateScriptRequest): Promise<GenerateScriptResponse> => {
    return client.post(`/scripts/${projectId}/generate`, data);
  },

  /**
   * 获取脚本
   * GET /api/v1/scripts/{project_id}
   */
  get: async (projectId: string): Promise<GetScriptResponse> => {
    return client.get(`/scripts/${projectId}`);
  },

  /**
   * 保存脚本
   * PUT /api/v1/scripts/{project_id}
   */
  save: async (projectId: string, data: UpdateScriptRequest): Promise<UpdateScriptResponse> => {
    return client.put(`/scripts/${projectId}`, data);
  },
};

export default scriptApi;
