/**
 * 任务状态管理
 * 管理异步任务进度
 */

import { create } from 'zustand';
import type { TaskId, TaskStatus } from '../types';

interface TaskInfo {
  taskId: TaskId;
  taskType: string;
  status: TaskStatus;
  progress: number;
  message: string;
}

interface TaskState {
  tasks: Map<TaskId, TaskInfo>;
  setTask: (task: TaskInfo) => void;
  updateTaskProgress: (taskId: TaskId, progress: number, message: string) => void;
  updateTaskStatus: (taskId: TaskId, status: TaskStatus) => void;
  removeTask: (taskId: TaskId) => void;
  clearTasks: () => void;
}

export const useTaskStore = create<TaskState>((set, get) => ({
  tasks: new Map(),
  setTask: (task) => {
    const tasks = new Map(get().tasks);
    tasks.set(task.taskId, task);
    set({ tasks });
  },
  updateTaskProgress: (taskId, progress, message) => {
    const tasks = new Map(get().tasks);
    const task = tasks.get(taskId);
    if (task) {
      tasks.set(taskId, { ...task, progress, message });
      set({ tasks });
    }
  },
  updateTaskStatus: (taskId, status) => {
    const tasks = new Map(get().tasks);
    const task = tasks.get(taskId);
    if (task) {
      tasks.set(taskId, { ...task, status });
      set({ tasks });
    }
  },
  removeTask: (taskId) => {
    const tasks = new Map(get().tasks);
    tasks.delete(taskId);
    set({ tasks });
  },
  clearTasks: () => set({ tasks: new Map() }),
}));
