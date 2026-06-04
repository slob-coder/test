/**
 * 媒体预览组件
 *
 * 用于展示图片/视频预览，支持加载状态和错误状态
 */

import React from 'react';
import { Image, Spin, Empty, Typography } from 'antd';
import { PlayCircleOutlined, FileImageOutlined } from '@ant-design/icons';
import type { Media } from '@/types';

const { Text } = Typography;

export interface MediaPreviewProps {
  media: Media | null | undefined;
  loading?: boolean;
  style?: React.CSSProperties;
  className?: string;
}

export const MediaPreview: React.FC<MediaPreviewProps> = ({
  media,
  loading = false,
  style,
  className,
}) => {
  if (loading) {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: 200,
          ...style,
        }}
        className={className}
      >
        <Spin tip="加载中..." />
      </div>
    );
  }

  if (!media) {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: 200,
          background: '#fafafa',
          borderRadius: 8,
          ...style,
        }}
        className={className}
      >
        <Empty
          image={<FileImageOutlined style={{ fontSize: 48, color: '#bfbfbf' }} />}
          description={<Text type="secondary">暂无媒体</Text>}
        />
      </div>
    );
  }

  if (media.status === 'generating') {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: 200,
          background: '#f0f5ff',
          borderRadius: 8,
          ...style,
        }}
        className={className}
      >
        <Spin tip="生成中..." />
      </div>
    );
  }

  if (media.status === 'failed') {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: 200,
          background: '#fff2f0',
          borderRadius: 8,
          ...style,
        }}
        className={className}
      >
        <Empty
          image={<FileImageOutlined style={{ fontSize: 48, color: '#ff4d4f' }} />}
          description={<Text type="danger">生成失败</Text>}
        />
      </div>
    );
  }

  if (media.media_type === 'image') {
    return (
      <Image
        src={media.file_url}
        alt="分镜图片"
        style={{ borderRadius: 8, maxHeight: 300, objectFit: 'cover', ...style }}
        className={className}
        placeholder
      />
    );
  }

  if (media.media_type === 'video') {
    return (
      <div
        style={{
          position: 'relative',
          borderRadius: 8,
          overflow: 'hidden',
          ...style,
        }}
        className={className}
      >
        <video
          src={media.file_url}
          controls
          style={{ width: '100%', borderRadius: 8 }}
        />
        {media.duration && (
          <Text
            type="secondary"
            style={{
              position: 'absolute',
              bottom: 8,
              right: 8,
              background: 'rgba(0,0,0,0.6)',
              color: '#fff',
              padding: '2px 8px',
              borderRadius: 4,
            }}
          >
            {media.duration.toFixed(1)}s
          </Text>
        )}
      </div>
    );
  }

  // TODO: 支持更多媒体类型
  return null;
};

export default MediaPreview;
