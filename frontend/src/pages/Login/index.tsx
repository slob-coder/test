/**
 * 登录页面
 * F01 用户注册与登录
 */

import React, { useState } from 'react';
import { Form, Input, Button, Card, message, Spin } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { useNavigate, Link } from 'react-router-dom';
import { useAuthStore } from '../../stores/authStore';

interface LoginForm {
  username: string;
  password: string;
}

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  const { login } = useAuthStore();

  const handleSubmit = async (values: LoginForm) => {
    setLoading(true);
    try {
      await login(values.username, values.password);
      message.success('登录成功');
      navigate('/projects');
    } catch (error: any) {
      const errorMessage = error?.response?.data?.message || '登录失败，请检查用户名和密码';
      message.error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      minHeight: '100vh',
      background: '#f0f2f5'
    }}>
      <Card title="🎬 AI视频生成 - 登录" style={{ width: 400 }}>
        <Spin spinning={loading}>
          <Form
            form={form}
            onFinish={handleSubmit}
            layout="vertical"
          >
            <Form.Item
              name="username"
              rules={[
                { required: true, message: '请输入用户名' },
                { min: 2, max: 50, message: '用户名长度为2-50个字符' },
              ]}
            >
              <Input 
                prefix={<UserOutlined />} 
                placeholder="请输入用户名" 
                size="large"
                maxLength={50}
              />
            </Form.Item>

            <Form.Item
              name="password"
              rules={[
                { required: true, message: '请输入密码' },
              ]}
            >
              <Input.Password
                prefix={<LockOutlined />}
                placeholder="请输入密码"
                size="large"
                maxLength={128}
              />
            </Form.Item>

            <Form.Item>
              <Button 
                type="primary" 
                htmlType="submit" 
                block 
                size="large"
                loading={loading}
                disabled={loading}
              >
                登录
              </Button>
            </Form.Item>

            <div style={{ textAlign: 'center' }}>
              还没有账号？ <Link to="/register">立即注册</Link>
            </div>
          </Form>
        </Spin>
      </Card>
    </div>
  );
};

export default LoginPage;
