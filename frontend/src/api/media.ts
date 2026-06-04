/**
 * M05: 媒体生成 API
 */

import client from './client';
import type {
  GenerateImageRequest,
  GenerateImageResponse,
  GenerateImagesRequest,
  GenerateVideoRequest,
  GenerateVideoResponse,
  MediaResponse,
} from '../types/media';

export const mediaApi = {
  /**
   * 生成单个分镜图片
   * POST /api/v1/media/generate-image
   */
  generateImage: async (data: GenerateImageRequest): Promise<GenerateImageResponse> => {
    return client.post('/media/generate-image', data);
  },

  /**
   * 批量生成图片
   * POST /api/v1/media/generate-images
   */
  generateImages: async (data: GenerateImagesRequest): Promise<GenerateImageResponse> => {
    return client.post('/media/generate-images', data);
  },

  /**
   * 生成单个视频片段
   * POST /api/v1/media/generate-video
   */
  generateVideo: async (data: GenerateVideoRequest): Promise<GenerateVideoResponse> => {
    return client.post('/media/generate-video', data);
  },

  /**
   * 批量生成视频
   * POST /api/v1/media/generate-videos
   */
  generateVideos: async (data: GenerateVideoRequest): Promise<GenerateVideoResponse> => {
    return client.post('/media/generate-videos', data);
  },

  /**
   * 上传替换图片
   * POST /api/v1/storyboard-items/{item_id}/upload-image
   */
  uploadImage: async (itemId: string, file: File): Promise<MediaResponse> => {
    const formData = new FormData();
    formData.append('file', file);
    return client.post(`/storyboard-items/${itemId}/upload-image`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },

  /**
   * 获取媒体文件信息
   * GET /api/v1/media/{media_id}
   */
  get: async (mediaId: string): Promise<MediaResponse> => {
    return client.get(`/media/${mediaId}`);
  },
};

export default mediaApi;
