import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './stores/authStore'

// 页面组件 - Lazy loading
const LoginPage = React.lazy(() => import('./pages/Login'))
const RegisterPage = React.lazy(() => import('./pages/Register'))
const ProjectListPage = React.lazy(() => import('./pages/ProjectList'))
const ProjectWorkspacePage = React.lazy(() => import('./pages/ProjectWorkspace'))

// 受保护的路由 - 未登录用户重定向到登录页
function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore()
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }
  
  return <>{children}</>
}

// 公开路由 - 已登录用户重定向到项目列表
function PublicRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore()
  
  if (isAuthenticated) {
    return <Navigate to="/projects" replace />
  }
  
  return <>{children}</>
}

// 布局组件 - TODO: 实现具体布局
function MainLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="main-layout">
      {/* TODO: 添加顶部导航栏 */}
      <main className="main-content">
        {children}
      </main>
    </div>
  )
}

// 加载中组件
function LoadingFallback() {
  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      minHeight: '100vh' 
    }}>
      Loading...
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <React.Suspense fallback={<LoadingFallback />}>
        <Routes>
          {/* 公开路由 - 已登录用户自动跳转 */}
          <Route 
            path="/login" 
            element={
              <PublicRoute>
                <LoginPage />
              </PublicRoute>
            } 
          />
          <Route 
            path="/register" 
            element={
              <PublicRoute>
                <RegisterPage />
              </PublicRoute>
            } 
          />
          
          {/* 受保护路由 - 未登录用户跳转登录页 */}
          <Route
            path="/projects"
            element={
              <ProtectedRoute>
                <MainLayout>
                  <ProjectListPage />
                </MainLayout>
              </ProtectedRoute>
            }
          />
          <Route
            path="/projects/:id/*"
            element={
              <ProtectedRoute>
                <MainLayout>
                  <ProjectWorkspacePage />
                </MainLayout>
              </ProtectedRoute>
            }
          />
          
          {/* 默认重定向 */}
          <Route path="/" element={<Navigate to="/projects" replace />} />
          <Route path="*" element={<Navigate to="/projects" replace />} />
        </Routes>
      </React.Suspense>
    </BrowserRouter>
  )
}

export default App
