/**
 * M04: 分镜管理 API
 */

import client from './client';
import type {
  GetStoryboardResponse,
  GenerateStoryboardRequest,
  GenerateStoryboardResponse,
  ReorderStoryboardRequest,
  CreateStoryboardItemRequest,
  UpdateStoryboardItemRequest,
  StoryboardItemResponse,
  SplitStoryboardItemRequest,
  MergeStoryboardItemsRequest,
} from '../types/storyboard';

export const storyboardApi = {
  /**
   * 获取分镜列表
   * GET /api/v1/projects/{project_id}/storyboard
   */
  get: async (projectId: string): Promise<GetStoryboardResponse> => {
    return client.get(`/projects/${projectId}/storyboard`);
  },

  /**
   * 从脚本生成分镜
   * POST /api/v1/projects/{project_id}/storyboard/generate
   */
  generate: async (projectId: string, data?: GenerateStoryboardRequest): Promise<GenerateStoryboardResponse> => {
    return client.post(`/projects/${projectId}/storyboard/generate`, data);
  },

  /**
   * 调整分镜顺序
   * PUT /api/v1/projects/{project_id}/storyboard/reorder
   */
  reorder: async (projectId: string, data: ReorderStoryboardRequest): Promise<void> => {
    return client.put(`/projects/${projectId}/storyboard/reorder`, data);
  },

  /**
   * 新增分镜项
   * POST /api/v1/storyboard-items
   */
  createItem: async (data: CreateStoryboardItemRequest): Promise<StoryboardItemResponse> => {
    return client.post('/storyboard-items', data);
  },

  /**
   * 更新分镜项
   * PUT /api/v1/storyboard-items/{item_id}
   */
  updateItem: async (itemId: string, data: UpdateStoryboardItemRequest): Promise<StoryboardItemResponse> => {
    return client.put(`/storyboard-items/${itemId}`, data);
  },

  /**
   * 删除分镜项
   * DELETE /api/v1/storyboard-items/{item_id}
   */
  deleteItem: async (itemId: string): Promise<void> => {
    return client.delete(`/storyboard-items/${itemId}`);
  },

  /**
   * 拆分分镜
   * POST /api/v1/storyboard-items/{item_id}/split
   */
  splitItem: async (itemId: string, data: SplitStoryboardItemRequest): Promise<StoryboardItemResponse[]> => {
    return client.post(`/storyboard-items/${itemId}/split`, data);
  },

  /**
   * 合并分镜
   * POST /api/v1/storyboard-items/merge
   */
  mergeItems: async (data: MergeStoryboardItemsRequest): Promise<StoryboardItemResponse> => {
    return client.post('/storyboard-items/merge', data);
  },
};

export default storyboardApi;
