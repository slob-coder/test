import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './stores/authStore'

// 页面组件 - TODO: 实现具体页面
const LoginPage = React.lazy(() => import('./pages/Login'))
const RegisterPage = React.lazy(() => import('./pages/Register'))
const ProjectListPage = React.lazy(() => import('./pages/ProjectList'))
const ProjectWorkspacePage = React.lazy(() => import('./pages/ProjectWorkspace'))

// 受保护的路由
function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore()
  
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
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

function App() {
  return (
    <BrowserRouter>
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          {/* 公开路由 */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          
          {/* 受保护路由 */}
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
