# 发布到 GitHub 快速指南

## 第一步：在 GitHub 创建仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `china-email-plugin` 或 `codex-china-email`
   - **Description**: `MCP plugin for Chinese email providers (QQ, 163, 139, etc.)`
   - **Visibility**: Public (推荐) 或 Private
   - **不要勾选**：Initialize with README, .gitignore, or license（我们已经有了）
3. 点击 "Create repository"

## 第二步：提交代码

在项目目录执行：

```bash
# 添加所有文件
git add .

# 提交（完整描述）
git commit -m "Initial commit: China Email MCP Plugin v1.0.0

- Support for QQ, NetEase, 139, Aliyun, Tencent email providers
- Email search, read, download attachments, send operations
- Comprehensive security hardening (8 major improvements)
- Path traversal protection and attachment size limits
- Complete test suite with 100% security test pass rate
- Full documentation (EN/CN) with security guides"
```

## 第三步：推送到 GitHub

```bash
# 关联远程仓库（替换为你的 GitHub 用户名和仓库名）
git remote add origin https://github.com/你的用户名/china-email-plugin.git

# 重命名分支为 main
git branch -M main

# 推送
git push -u origin main
```

## 第四步：创建 Release

1. 在 GitHub 仓库页面，点击 **Releases** → **Create a new release**
2. 填写：
   - **Tag**: `v1.0.0`
   - **Release title**: `v1.0.0 - Initial Release`
   - **Description**: 
   
```markdown
## 🎉 首次发布

### 功能特性
- ✅ 支持主流国内邮箱：QQ、网易（163/126）、139、阿里云、腾讯企业邮箱
- ✅ 完整的邮件操作：搜索、读取、附件下载、发送（带双重确认）
- ✅ 友好的本地 Web 配置向导

### 安全特性
- 🔒 企业级安全加固（8 大类改进）
- 🔒 路径穿越防护
- 🔒 附件大小限制（50MB/文件，100MB/总计）
- 🔒 SSL/TLS 加密连接
- 🔒 严格的输入验证和清理

### 安装

```bash
git clone https://github.com/你的用户名/china-email-plugin.git
cd china-email-plugin
pip install -e .
python -m china_email_mcp setup
```

### 文档
- [Installation Guide](./INSTALLATION_GUIDE.md)
- [Security Improvements](./SECURITY_IMPROVEMENTS.md)
- [Security Checklist](./SECURITY_CHECKLIST.md)

### 测试状态
✅ 所有安全测试通过
```

3. 点击 **Publish release**

## 第五步：更新 README 中的 GitHub 链接

发布后，记得将 README.md 中的占位符 `yourusername` 替换为实际的 GitHub 用户名：

```bash
# 在 README.md 中查找并替换
github.com/yourusername/china-email-plugin
# 改为
github.com/你的实际用户名/china-email-plugin

git add README.md
git commit -m "docs: update GitHub links in README"
git push
```

## 验证发布

发布成功后：

1. ✅ 仓库页面显示所有文件
2. ✅ README.md 正确渲染
3. ✅ Release v1.0.0 可见
4. ✅ 其他用户可以克隆

## 用户安装方式

发布后，用户可以这样安装：

```bash
# 方式1：克隆安装
git clone https://github.com/你的用户名/china-email-plugin.git
cd china-email-plugin
pip install -e .

# 方式2：直接从 GitHub 安装（如果配置了 setup.py）
pip install git+https://github.com/你的用户名/china-email-plugin.git
```

## 后续维护

### 提交新更改
```bash
git add .
git commit -m "feat: add new feature"
git push
```

### 发布新版本
```bash
# 更新 CHANGELOG.md
# 提交更改
git add CHANGELOG.md
git commit -m "chore: prepare v1.0.1 release"
git push

# 打标签
git tag v1.0.1
git push origin v1.0.1

# 在 GitHub 创建新 Release
```

---

**注意事项**：
- ⚠️ 确保没有提交敏感信息（查看 .gitignore）
- ⚠️ 推送前检查 `git status` 和 `git log`
- ⚠️ 首次推送可能需要 GitHub 身份验证
