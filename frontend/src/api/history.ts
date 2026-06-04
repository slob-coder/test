/**
 * M08: 历史记录 API
 */

import client from './client';
import type {
  ListHistoriesResponse,
  GetHistoryResponse,
} from '../types/history';

export const historyApi = {
  /**
   * 获取项目历史记录
   * GET /api/v1/projects/{project_id}/histories
   */
  list: async (projectId: string): Promise<ListHistoriesResponse> => {
    return client.get(`/projects/${projectId}/histories`);
  },

  /**
   * 获取历史详情
   * GET /api/v1/histories/{history_id}
   */
  get: async (historyId: string): Promise<GetHistoryResponse> => {
    return client.get(`/histories/${historyId}`);
  },
};

export default historyApi;
