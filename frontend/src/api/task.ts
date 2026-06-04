/**
 * M10: 任务状态 API
 */

import client from './client';
import type {
  TaskStatusResponse,
  ListTasksResponse,
  TaskProgressEvent,
  TaskCompletedEvent,
  TaskFailedEvent,
} from '../types/task';

export const taskApi = {
  /**
   * 查询任务状态
   * GET /api/v1/tasks/{task_id}/status
   */
  getStatus: async (taskId: string): Promise<TaskStatusResponse> => {
    return client.get(`/tasks/${taskId}/status`);
  },

  /**
   * 查询当前用户所有任务
   * GET /api/v1/tasks
   */
  list: async (): Promise<ListTasksResponse> => {
    return client.get('/tasks');
  },

  /**
   * SSE 订阅任务进度
   * GET /api/v1/tasks/{task_id}/stream
   * 返回 EventSource 实例
   */
  subscribe: (taskId: string): EventSource => {
    const baseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';
    const url = `${baseUrl}/tasks/${taskId}/stream`;
    return new EventSource(url);
  },
};

// SSE 事件类型
export type TaskEvent = TaskProgressEvent | TaskCompletedEvent | TaskFailedEvent;

// SSE 事件类型守卫
export const isProgressEvent = (event: TaskEvent): event is TaskProgressEvent => {
  return 'progress' in event;
};

export const isCompletedEvent = (event: TaskEvent): event is TaskCompletedEvent => {
  return 'result' in event;
};

export const isFailedEvent = (event: TaskEvent): event is TaskFailedEvent => {
  return 'error' in event;
};

export default taskApi;
