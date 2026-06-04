/**
 * M06: 字幕生成 API
 */

import client from './client';
import type {
  GenerateSubtitlesRequest,
  GenerateSubtitlesResponse,
  GetSubtitlesResponse,
  UpdateSubtitleEntryRequest,
  SubtitleEntryResponse,
} from '../types/subtitle';

export const subtitleApi = {
  /**
   * 自动生成字幕
   * POST /api/v1/projects/{project_id}/subtitles/generate
   */
  generate: async (projectId: string, data?: GenerateSubtitlesRequest): Promise<GenerateSubtitlesResponse> => {
    return client.post(`/projects/${projectId}/subtitles/generate`, data);
  },

  /**
   * 获取字幕列表
   * GET /api/v1/projects/{project_id}/subtitles
   */
  list: async (projectId: string): Promise<GetSubtitlesResponse> => {
    return client.get(`/projects/${projectId}/subtitles`);
  },

  /**
   * 更新字幕条目
   * PUT /api/v1/subtitles/{subtitle_id}
   */
  updateEntry: async (subtitleId: string, data: UpdateSubtitleEntryRequest): Promise<SubtitleEntryResponse> => {
    return client.put(`/subtitles/${subtitleId}`, data);
  },

  /**
   * 导出 SRT 文件
   * GET /api/v1/projects/{project_id}/subtitles/export
   */
  exportSrt: async (projectId: string): Promise<Blob> => {
    const response = await client.get(`/projects/${projectId}/subtitles/export`, {
      responseType: 'blob',
    });
    return response as unknown as Blob;
  },

  /**
   * 删除项目全部字幕
   * DELETE /api/v1/projects/{project_id}/subtitles
   */
  deleteAll: async (projectId: string): Promise<void> => {
    return client.delete(`/projects/${projectId}/subtitles`);
  },
};

export default subtitleApi;
