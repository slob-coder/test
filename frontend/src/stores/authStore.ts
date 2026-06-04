/**
 * 认证状态管理
 * 使用 Zustand 管理用户登录状态
 */

import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { authApi } from '../api/auth';
import type { UserDTO } from '../types';

interface AuthState {
  user: UserDTO | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  
  // Actions
  login: (username: string, password: string) => Promise<void>;
  register: (username: string, password: string) => Promise<void>;
  logout: () => void;
  fetchCurrentUser: () => Promise<void>;
  refreshToken: () => Promise<void>;
  setUser: (user: UserDTO) => void;
  setToken: (token: string) => void;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,
      isLoading: false,
      error: null,

      login: async (username: string, password: string) => {
        set({ isLoading: true, error: null });
        try {
          const response = await authApi.login({ username, password });
          localStorage.setItem('access_token', response.access_token);
          set({
            user: response.user,
            token: response.access_token,
            isAuthenticated: true,
            isLoading: false,
          });
        } catch (error: unknown) {
          const errorMessage = error instanceof Error ? error.message : '登录失败';
          set({ isLoading: false, error: errorMessage });
          throw error;
        }
      },

      register: async (username: string, password: string) => {
        set({ isLoading: true, error: null });
        try {
          await authApi.register({ username, password });
          set({ isLoading: false });
        } catch (error: unknown) {
          const errorMessage = error instanceof Error ? error.message : '注册失败';
          set({ isLoading: false, error: errorMessage });
          throw error;
        }
      },

      logout: () => {
        localStorage.removeItem('access_token');
        set({
          user: null,
          token: null,
          isAuthenticated: false,
          error: null,
        });
      },

      fetchCurrentUser: async () => {
        const token = get().token || localStorage.getItem('access_token');
        if (!token) {
          set({ isAuthenticated: false });
          return;
        }
        
        try {
          const user = await authApi.getMe();
          set({
            user,
            token,
            isAuthenticated: true,
          });
        } catch {
          localStorage.removeItem('access_token');
          set({
            user: null,
            token: null,
            isAuthenticated: false,
          });
        }
      },

      refreshToken: async () => {
        try {
          const response = await authApi.refreshToken();
          localStorage.setItem('access_token', response.access_token);
          set({ token: response.access_token });
        } catch {
          get().logout();
        }
      },

      setUser: (user: UserDTO) => set({ user, isAuthenticated: true }),
      setToken: (token: string) => {
        localStorage.setItem('access_token', token);
        set({ token });
      },
      clearError: () => set({ error: null }),
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        user: state.user,
        token: state.token,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
