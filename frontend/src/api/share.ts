/**
 * M09: 导出分享 API
 */

import client from './client';
import type {
  ExportVideoRequest,
  ExportVideoResponse,
  CreateShareLinkResponse,
  GetSharedVideoResponse,
} from '../types/share';

export const shareApi = {
  /**
   * 导出视频
   * POST /api/v1/compositions/{composition_id}/export
   */
  exportVideo: async (compositionId: string, data?: ExportVideoRequest): Promise<ExportVideoResponse> => {
    return client.post(`/compositions/${compositionId}/export`, data);
  },

  /**
   * 生成分享链接
   * POST /api/v1/compositions/{composition_id}/share
   */
  createShareLink: async (compositionId: string): Promise<CreateShareLinkResponse> => {
    return client.post(`/compositions/${compositionId}/share`);
  },

  /**
   * 访问分享视频（无需登录）
   * GET /api/v1/share/{token}
   */
  getSharedVideo: async (token: string): Promise<GetSharedVideoResponse> => {
    return client.get(`/share/${token}`);
  },
};

export default shareApi;
