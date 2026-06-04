/**
 * 进度条组件
 * 用于展示任务进度
 */

import React from 'react';
import { Progress, Card, Typography, Space } from 'antd';

const { Text } = Typography;

export interface ProgressBarProps {
  percent: number;
  status?: 'active' | 'success' | 'exception';
  message?: string;
  showInfo?: boolean;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({
  percent,
  status = 'active',
  message,
  showInfo = true,
}) => {
  // TODO: 实现进度条动画效果
  return (
    <Card size="small" style={{ marginBottom: 16 }}>
      <Space direction="vertical" style={{ width: '100%' }}>
        <Progress
          percent={percent}
          status={status}
          showInfo={showInfo}
          strokeColor={{
            '0%': '#108ee9',
            '100%': '#87d068',
          }}
        />
        {message && (
          <Text type="secondary" style={{ fontSize: 12 }}>
            {message}
          </Text>
        )}
      </Space>
    </Card>
  );
};

export default ProgressBar;
