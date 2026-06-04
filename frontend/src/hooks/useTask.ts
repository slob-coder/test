/**
 * 任务状态 Hook
 *
 * 用于查询和管理异步任务状态
 */

import { useQuery, useQueryClient } from '@tanstack/react-query';
import { taskApi } from '../api/task';
import type { TaskStatus } from '../types';

interface UseTaskOptions {
  taskId: string;
  enabled?: boolean;
  refetchInterval?: number;
}

export function useTask(options: UseTaskOptions) {
  const { taskId, enabled = true, refetchInterval } = options;

  const query = useQuery({
    queryKey: ['task', taskId],
    queryFn: () => taskApi.getTaskStatus(taskId),
    enabled: enabled && !!taskId,
    refetchInterval: (data) => {
      // 任务完成或失败后停止轮询
      if (data?.status === 'completed' || data?.status === 'failed') {
        return false;
      }
      return refetchInterval || 2000;
    },
  });

  return {
    task: query.data,
    isLoading: query.isLoading,
    error: query.error,
    refetch: query.refetch,
  };
}

export function useTaskList() {
  const query = useQuery({
    queryKey: ['tasks'],
    queryFn: () => taskApi.getTasks(),
  });

  return {
    tasks: query.data || [],
    isLoading: query.isLoading,
    error: query.error,
    refetch: query.refetch,
  };
}

export function useTaskActions() {
  const queryClient = useQueryClient();

  const invalidateTask = (taskId: string) => {
    queryClient.invalidateQueries({ queryKey: ['task', taskId] });
  };

  const invalidateAllTasks = () => {
    queryClient.invalidateQueries({ queryKey: ['tasks'] });
  };

  return {
    invalidateTask,
    invalidateAllTasks,
  };
}

export default useTask;
