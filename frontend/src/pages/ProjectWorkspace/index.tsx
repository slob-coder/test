/**
 * 项目工作台页面
 * 
 * 核心页面，包含：
 * - 顶部导航栏：项目名称、步骤条、保存状态
 * - 左侧场景列表
 * - 主编辑区（脚本编辑/分镜卡片/视频预览）
 * - 底部属性面板
 */

import React from 'react';
import { useParams, Outlet } from 'react-router-dom';
import { Layout, Steps, Button, Space, Typography } from 'antd';
import {
  FileTextOutlined,
  AppstoreOutlined,
  VideoCameraOutlined,
  HistoryOutlined,
} from '@ant-design/icons';

const { Header, Sider, Content } = Layout;
const { Title } = Typography;

/** 步骤条配置 */
const STEPS = [
  { title: '脚本', icon: <FileTextOutlined /> },
  { title: '分镜', icon: <AppstoreOutlined /> },
  { title: '合成', icon: <VideoCameraOutlined /> },
  { title: '完成', icon: <HistoryOutlined /> },
];

/** 项目工作台组件 */
const ProjectWorkspace: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [currentStep, setCurrentStep] = React.useState(0);

  // TODO: 从 API 获取项目数据
  // TODO: 实现步骤切换逻辑
  // TODO: 实现左侧场景列表
  // TODO: 实现主编辑区内容切换

  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* 顶部导航栏 */}
      <Header style={{ 
        background: '#fff', 
        padding: '0 24px',
        borderBottom: '1px solid #f0f0f0',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}>
        <Title level={4} style={{ margin: 0 }}>
          项目: {id}
        </Title>
        
        <Steps 
          current={currentStep} 
          onChange={setCurrentStep}
          items={STEPS}
          style={{ flex: 1, maxWidth: 600, margin: '0 48px' }}
        />
        
        <Space>
          <span style={{ color: '#52c41a' }}>已保存</span>
          <Button type="primary">导出</Button>
        </Space>
      </Header>

      <Layout>
        {/* 左侧场景列表 */}
        <Sider 
          width={240} 
          theme="light"
          style={{ borderRight: '1px solid #f0f0f0' }}
        >
          <div style={{ padding: '16px' }}>
            <Title level={5}>场景列表</Title>
            {/* TODO: 场景列表组件 */}
            <div style={{ color: '#999', marginTop: 16 }}>
              场景列表待实现
            </div>
          </div>
        </Sider>

        {/* 主编辑区 */}
        <Content style={{ background: '#fff' }}>
          <Outlet />
        </Content>
      </Layout>
    </Layout>
  );
};

export default ProjectWorkspace;
