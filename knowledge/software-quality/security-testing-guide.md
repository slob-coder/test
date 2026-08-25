# Web 应用安全测试指南

> 基于 OWASP Top 10 和常见漏洞模式。
> 适用于 REST API + SPA 架构的 Web 应用。

---

## 1. 注入类漏洞

### SQL 注入
**测试手法**：在所有用户输入字段尝试注入 payload

```
常用 payload:
' OR '1'='1
' OR '1'='1' --
' UNION SELECT null,null,null --
1; DROP TABLE users --
' AND SLEEP(5) --        # 盲注时间检测
```

**测试点**：
- 所有查询参数（URL query string）
- 所有表单字段
- HTTP Header（X-Forwarded-For, Referer 等）
- JSON 请求体中的字符串字段
- 排序字段（ORDER BY 注入）
- 分页参数（LIMIT/OFFSET 注入）

**预期**：返回参数校验错误（400），不返回数据库错误信息

### XSS（跨站脚本）
```
常用 payload:
<script>alert('xss')</script>
<img src=x onerror=alert(1)>
"><script>alert(document.cookie)</script>
javascript:alert(1)
' onmouseover='alert(1)'
```

**测试点**：
- 所有在页面上显示的用户输入（用户名、评论、标题等）
- URL 参数被反射到页面上的场景
- Markdown/Rich Text 渲染
- 搜索结果高亮

### 命令注入
```
常用 payload:
; ls -la
| cat /etc/passwd
$(whoami)
`id`
```

**测试点**：涉及系统命令执行的功能（文件操作、Git 操作、Shell 执行等）

### SSRF（服务端请求伪造）
```
测试 URL:
http://127.0.0.1:8000/admin
http://169.254.169.254/latest/meta-data/    # AWS 元数据
http://[::1]/
file:///etc/passwd
```

**测试点**：所有接受 URL 参数的接口（回调、头像、导入等）

---

## 2. 认证与授权

### 认证测试
- [ ] 空用户名/空密码能否登录
- [ ] 密码错误 N 次后是否锁定/延迟
- [ ] 登录接口是否有频率限制
- [ ] Token/Session 过期后是否拒绝请求
- [ ] 注销后 Token 是否失效（再次使用应返回 401）
- [ ] 修改密码后旧 Token 是否失效
- [ ] 弱密码能否通过注册（如 123456、password）

### 水平越权（IDOR）
**核心手法**：修改请求中的资源 ID，尝试访问他人数据

```
# 用户 A 的 token 访问用户 B 的资源
GET /api/users/USER_B_ID/profile     # 应 403 或只返回公开信息
PUT /api/orders/OTHER_USER_ORDER_ID  # 应 403
DELETE /api/posts/OTHER_USER_POST_ID # 应 403
```

**测试点**：所有带资源 ID 的接口（路径参数、查询参数、请求体中的 ID）

### 垂直越权
**核心手法**：用低权限用户的 Token 访问高权限接口

```
# 普通用户 Token 访问管理接口
GET /api/admin/users
POST /api/admin/settings
DELETE /api/admin/users/xxx
```

---

## 3. 会话管理

- [ ] Token 是否有合理的过期时间（不过长）
- [ ] Refresh Token 机制是否安全
- [ ] 同一账号多处登录的控制策略
- [ ] Token 是否在 URL 中传递（不应该）
- [ ] Cookie 是否设置 HttpOnly, Secure, SameSite
- [ ] 会话固定：登录前后 Session ID 是否变化

---

## 4. 敏感信息保护

- [ ] API 响应中是否泄露密码哈希、内部 ID、堆栈信息
- [ ] 错误响应是否暴露 SQL 语句、文件路径、服务器版本
- [ ] 日志中是否记录了密码、Token、信用卡号
- [ ] 敏感接口（密码修改、支付等）是否通过 HTTPS
- [ ] CORS 配置是否过于宽松（Access-Control-Allow-Origin: *）
- [ ] 响应头是否包含安全头（X-Content-Type-Options, X-Frame-Options 等）

---

## 5. 文件上传安全

- [ ] 是否限制文件类型（白名单而非黑名单）
- [ ] 是否检查文件 MIME type（不只看扩展名）
- [ ] 是否限制文件大小
- [ ] 上传 .php / .jsp / .html 能否被执行
- [ ] 文件名是否做了清洗（防止路径遍历 `../../etc/passwd`）
- [ ] 上传后的文件是否在非 web 可访问目录

---

## 6. API 接口安全

- [ ] 所有写操作接口是否需要认证
- [ ] 接口是否有频率限制（防刷）
- [ ] 批量操作是否有数量限制
- [ ] 是否防重放攻击（时间戳 + nonce）
- [ ] GraphQL 接口是否禁用了 introspection（生产环境）
- [ ] WebSocket 连接是否验证身份
- [ ] 导出接口是否限制数据量（防止全量导出）

---

## 7. 业务逻辑安全

- [ ] 金额是否由服务端计算（不信任客户端传入的金额）
- [ ] 优惠/折扣是否有防重复使用机制
- [ ] 库存扣减是否防超卖（并发安全）
- [ ] 订单状态流转是否严格校验（不能从已完成跳回已支付）
- [ ] 关键操作是否有二次确认/验证码
