/**
 * 项目状态管理
 * 管理当前项目上下文
 */

import { create } from 'zustand';
import type { ProjectId, ProjectStatus } from '../types';

interface ProjectState {
  currentProjectId: ProjectId | null;
  projectStatus: ProjectStatus | null;
  setCurrentProject: (projectId: ProjectId, status: ProjectStatus) => void;
  updateStatus: (status: ProjectStatus) => void;
  clearProject: () => void;
}

export const useProjectStore = create<ProjectState>((set) => ({
  currentProjectId: null,
  projectStatus: null,
  setCurrentProject: (projectId, status) =>
    set({ currentProjectId: projectId, projectStatus: status }),
  updateStatus: (status) => set({ projectStatus: status }),
  clearProject: () =>
    set({ currentProjectId: null, projectStatus: null }),
}));
