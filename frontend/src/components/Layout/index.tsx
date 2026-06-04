/**
 * 布局组件
 * 提供统一的页面布局结构
 */

import React from 'react';
import { Layout as AntLayout, Menu, Dropdown, Avatar, Button } from 'antd';
import {
  UserOutlined,
  LogoutOutlined,
  ProjectOutlined,
} from '@ant-design/icons';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuthStore } from '../../stores/authStore';

const { Header, Content, Sider } = AntLayout;

interface LayoutProps {
  children: React.ReactNode;
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useAuthStore();

  const handleLogout = () => {
    // TODO: 实现登出逻辑
    logout();
    navigate('/login');
  };

  const userMenu = (
    <Menu>
      <Menu.Item key="logout" icon={<LogoutOutlined />} onClick={handleLogout}>
        退出登录
      </Menu.Item>
    </Menu>
  );

  return (
    <AntLayout style={{ minHeight: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <ProjectOutlined style={{ fontSize: '24px', color: '#fff', marginRight: '12px' }} />
          <span style={{ color: '#fff', fontSize: '18px', fontWeight: 'bold' }}>
            AI视频生成
          </span>
        </div>
        {user && (
          <Dropdown overlay={userMenu} placement="bottomRight">
            <div style={{ cursor: 'pointer', display: 'flex', alignItems: 'center' }}>
              <Avatar icon={<UserOutlined />} style={{ marginRight: '8px' }} />
              <span style={{ color: '#fff' }}>{user.username}</span>
            </div>
          </Dropdown>
        )}
      </Header>
      <Content style={{ padding: '24px' }}>
        {children}
      </Content>
    </AntLayout>
  );
};

export default Layout;
