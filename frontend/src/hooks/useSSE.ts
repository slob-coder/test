/**
 * SSE 连接 Hook
 *
 * 用于订阅任务进度推送
 */

import { useEffect, useRef, useCallback } from 'react';

interface SSEOptions {
  url: string;
  onProgress?: (data: { task_id: string; progress: number; message: string }) => void;
  onCompleted?: (data: { task_id: string; result: Record<string, unknown> }) => void;
  onFailed?: (data: { task_id: string; error: string }) => void;
  onError?: (error: Event) => void;
}

export function useSSE(options: SSEOptions) {
  const eventSourceRef = useRef<EventSource | null>(null);

  const connect = useCallback(() => {
    // TODO: 实现 SSE 连接逻辑
    const eventSource = new EventSource(options.url);
    eventSourceRef.current = eventSource;

    eventSource.addEventListener('progress', (event) => {
      // TODO: 解析并调用 onProgress
      console.log('SSE progress:', event.data);
    });

    eventSource.addEventListener('completed', (event) => {
      // TODO: 解析并调用 onCompleted
      console.log('SSE completed:', event.data);
    });

    eventSource.addEventListener('failed', (event) => {
      // TODO: 解析并调用 onFailed
      console.log('SSE failed:', event.data);
    });

    eventSource.onerror = (error) => {
      options.onError?.(error);
    };
  }, [options]);

  const disconnect = useCallback(() => {
    if (eventSourceRef.current) {
      eventSourceRef.current.close();
      eventSourceRef.current = null;
    }
  }, []);

  useEffect(() => {
    return () => {
      disconnect();
    };
  }, [disconnect]);

  return { connect, disconnect };
}

export default useSSE;
