# AI 视频生成应用

基于 AI 的视频自动生成平台，支持脚本生成、分镜管理、媒体生成、字幕生成和视频合成。

## 技术栈

### 前端
- React 18 + TypeScript
- Vite (构建工具)
- Ant Design (UI 组件库)
- Zustand (状态管理)
- TanStack Query (服务端状态)
- Axios (HTTP 客户端)

### 后端
- Python 3.11+
- FastAPI (Web 框架)
- SQLAlchemy (ORM)
- Alembic (数据库迁移)
- Celery (异步任务)
- Redis (缓存 + 消息队列)

### 数据库与存储
- PostgreSQL 15
- MinIO (对象存储)

## 项目结构

```
.
├── frontend/                # 前端项目
│   ├── src/
│   │   ├── api/            # API 调用封装
│   │   ├── components/     # 通用组件
│   │   ├── hooks/          # 自定义 Hooks
│   │   ├── pages/          # 页面组件
│   │   ├── stores/         # Zustand 状态管理
│   │   ├── types/          # TypeScript 类型定义
│   │   └── utils/          # 工具函数
│   ├── package.json
│   └── vite.config.ts
│
├── backend/                 # 后端项目
│   ├── app/
│   │   ├── api/            # API 路由
│   │   ├── models/         # SQLAlchemy 模型
│   │   ├── schemas/        # Pydantic 模型
│   │   ├── services/       # 业务逻辑
│   │   ├── tasks/          # Celery 任务
│   │   ├── ai/             # AI 服务封装
│   │   └── utils/          # 工具函数
│   ├── alembic/            # 数据库迁移
│   ├── tests/              # 测试
│   └── pyproject.toml
│
├── docker-compose.yml       # Docker Compose 配置
└── .github/
    └── workflows/
        └── ci.yml          # CI 配置
```

## 快速开始

### 环境要求

- Docker & Docker Compose
- Node.js 18+ (本地开发)
- Python 3.11+ (本地开发)

### 使用 Docker Compose 启动

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

服务启动后：
- 前端: http://localhost
- 后端 API: http://localhost/api/v1
- API 文档: http://localhost/api/docs

### 本地开发

#### 后端

```bash
cd backend

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -e ".[dev]"

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 数据库迁移
alembic upgrade head

# 启动开发服务器
uvicorn app.main:app --reload --port 8000

# 启动 Celery Worker (另一个终端)
celery -A app.celery_app worker --loglevel=info
```

#### 前端

```bash
cd frontend

# 安装依赖
pnpm install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 启动开发服务器
pnpm dev
```

## 环境变量

### 后端 (.env)

```env
# 应用配置
APP_NAME=AI视频生成应用
APP_ENV=development
DEBUG=true
SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:3000

# 数据库
DATABASE_URL=postgresql+asyncpg://aivideo:aivideo@localhost:5432/aivideo

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
JWT_SECRET_KEY=your-jwt-secret
JWT_ALGORITHM=HS256
JWT_EXPIRE_HOURS=24

# AI 服务
OPENAI_API_KEY=your-openai-key
AI_MODEL_SCRIPT=gpt-4o-mini
AI_MODEL_IMAGE=dall-e-3

# 文件存储
STORAGE_TYPE=local
UPLOAD_DIR=./uploads
```

### 前端 (.env)

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_TITLE=AI视频生成
```

## API 文档

启动后端服务后，访问以下地址查看 API 文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 功能模块

| 模块 | 功能 |
|------|------|
| M01 认证 | 用户注册、登录、Token 管理 |
| M02 项目管理 | 项目 CRUD、状态管理 |
| M03 脚本生成 | AI 生成脚本、脚本编辑 |
| M04 分镜管理 | 分镜拆分、排序、合并 |
| M05 媒体生成 | AI 生成图片/视频、素材上传 |
| M06 字幕生成 | 自动生成字幕、时间轴调整 |
| M07 视频合成 | FFmpeg 视频拼接、字幕叠加 |
| M08 历史记录 | 操作历史、版本快照 |
| M09 导出分享 | 视频导出、分享链接 |
| M10 任务状态 | 异步任务状态、SSE 推送 |

## 开发指南

### 代码规范

- 前端: ESLint + Prettier
- 后端: Ruff (lint + format)
- 提交信息: Conventional Commits

### 测试

```bash
# 后端测试
cd backend
pytest tests/ -v

# 前端测试
cd frontend
pnpm test
```

## License

MIT
