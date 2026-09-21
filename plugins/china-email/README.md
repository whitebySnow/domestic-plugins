<<<<<<< HEAD
# China Email MCP Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A Model Context Protocol (MCP) plugin for Chinese email providers, enabling seamless email operations through Codex and other MCP-compatible AI assistants.

[English](#english) | [中文](#中文)

---

## English

### Features

- **Multi-Provider Support**: QQ Mail, NetEase (163/126), 139 Mail, Aliyun, Tencent Corporate Mail
- **Complete Email Operations**:
  - Search emails with IMAP queries
  - Read email content (HTML/plain text)
  - Download attachments (batch support)
  - Create drafts
  - Send emails (with safety confirmations)
- **Security Hardened**:
  - Path traversal protection
  - Attachment size limits (50MB/file, 100MB total)
  - SSL/TLS encryption
  - Credential protection (0600 permissions)
  - Double confirmation for sending
- **User-Friendly**: Web-based setup wizard with pre-configured providers

### Installation

#### Requirements
- Python 3.10 or higher
- Codex or any MCP-compatible client

#### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/china-email-plugin.git
cd china-email-plugin

# Install dependencies
pip install -r requirements.txt

# Install the plugin
pip install -e .

# Run setup wizard
python -m china_email_mcp setup
```

#### Codex Configuration

Add to your `~/.codex/config.toml`:

```toml
[mcp_servers.china_email]
type = "stdio"
command = "python"
args = ["-m", "china_email_mcp"]
```

Restart Codex and the plugin will be available.

### Quick Examples

Once configured, use natural language in Codex:

```
Show me the last 5 emails from my QQ mailbox
```

```
Search for emails with subject containing "invoice"
```

```
Download all attachments from email UID 123 to ~/Downloads
```

```
Send an email to example@qq.com with subject "Hello" (draft mode)
```

### Supported Providers

| Provider | IMAP Server | SMTP Server | Authorization |
|----------|-------------|-------------|---------------|
| QQ Mail | imap.qq.com:993 | smtp.qq.com:465 | App-specific password |
| NetEase (163) | imap.163.com:993 | smtp.163.com:465 | App-specific password |
| 139 Mail | imap.139.com:993 | smtp.139.com:465 | App-specific password |
| Aliyun | imap.aliyun.com:993 | smtp.aliyun.com:465 | App-specific password |
| Tencent Corp | imap.exmail.qq.com:993 | smtp.exmail.qq.com:465 | App-specific password |

### Getting Authorization Codes

Most Chinese email providers require app-specific passwords instead of login passwords:

- **QQ Mail**: Settings → Account → POP3/IMAP/SMTP → Generate authorization code
- **NetEase**: Settings → POP3/SMTP/IMAP → Enable service → Get authorization password
- **139 Mail**: Settings → Mail settings → Client authorization password

### Security

This plugin implements enterprise-grade security:

- ✅ All connections use SSL/TLS encryption
- ✅ Path traversal attack prevention
- ✅ Attachment size limits to prevent DoS
- ✅ Strict input validation and sanitization
- ✅ Secure credential storage with proper permissions
- ✅ Double confirmation before sending emails
- ✅ Error message sanitization to prevent info leakage

See [SECURITY_IMPROVEMENTS.md](./SECURITY_IMPROVEMENTS.md) for details.

### Documentation

- [Installation Guide](./INSTALLATION_GUIDE.md) - Complete setup instructions
- [Security Improvements](./SECURITY_IMPROVEMENTS.md) - Security hardening details
- [Security Checklist](./SECURITY_CHECKLIST.md) - Deployment and maintenance guide
- [Changelog](./CHANGELOG.md) - Version history

### Testing

```bash
# Run security tests
python tests/test_security_improvements.py

# Run all tests (if pytest configured)
pytest tests/
```

### Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Security Issues

If you discover a security vulnerability, please email the maintainer privately instead of opening a public issue.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 中文

### 功能特性

- **多邮箱支持**：QQ 邮箱、网易邮箱（163/126）、139 邮箱、阿里云邮箱、腾讯企业邮箱
- **完整邮件操作**：
  - 使用 IMAP 查询搜索邮件
  - 读取邮件内容（HTML/纯文本）
  - 下载附件（支持批量）
  - 创建草稿
  - 发送邮件（带安全确认）
- **安全加固**：
  - 路径穿越防护
  - 附件大小限制（单文件 50MB，总计 100MB）
  - SSL/TLS 加密
  - 凭证保护（0600 权限）
  - 发送邮件双重确认
- **用户友好**：基于 Web 的配置向导，预配置主流邮箱提供商

### 安装

#### 环境要求
- Python 3.10 或更高版本
- Codex 或任何兼容 MCP 的客户端

#### 快速开始

```bash
# 克隆仓库
git clone https://github.com/yourusername/china-email-plugin.git
cd china-email-plugin

# 安装依赖
pip install -r requirements.txt

# 安装插件
pip install -e .

# 运行配置向导
python -m china_email_mcp setup
```

#### Codex 配置

在 `~/.codex/config.toml` 中添加：

```toml
[mcp_servers.china_email]
type = "stdio"
command = "python"
args = ["-m", "china_email_mcp"]
```

重启 Codex 后插件即可使用。

### 使用示例

配置完成后，在 Codex 中使用自然语言：

```
显示我 QQ 邮箱最近 5 封邮件
```

```
搜索主题包含"发票"的邮件
```

```
下载邮件 UID 123 的所有附件到 ~/Downloads
```

```
给 example@qq.com 发送主题为"你好"的邮件（草稿模式）
```

### 支持的邮箱提供商

| 提供商 | IMAP 服务器 | SMTP 服务器 | 授权方式 |
|--------|------------|------------|---------|
| QQ 邮箱 | imap.qq.com:993 | smtp.qq.com:465 | 授权码 |
| 网易邮箱 | imap.163.com:993 | smtp.163.com:465 | 授权密码 |
| 139 邮箱 | imap.139.com:993 | smtp.139.com:465 | 客户端授权密码 |
| 阿里云邮箱 | imap.aliyun.com:993 | smtp.aliyun.com:465 | 授权码 |
| 腾讯企业邮箱 | imap.exmail.qq.com:993 | smtp.exmail.qq.com:465 | 授权码 |

### 获取授权码

大部分国内邮箱需要使用授权码而非登录密码：

- **QQ 邮箱**：设置 → 账户 → POP3/IMAP/SMTP 服务 → 生成授权码
- **网易邮箱**：设置 → POP3/SMTP/IMAP → 开启服务 → 获取授权密码
- **139 邮箱**：设置 → 邮箱设置 → 客户端授权密码

### 安全性

本插件实现了企业级安全防护：

- ✅ 所有连接使用 SSL/TLS 加密
- ✅ 路径穿越攻击防护
- ✅ 附件大小限制防止 DoS
- ✅ 严格的输入验证和清理
- ✅ 安全的凭证存储（0600 权限）
- ✅ 发送邮件前双重确认
- ✅ 错误信息脱敏防止信息泄露

详见 [SECURITY_IMPROVEMENTS.md](./SECURITY_IMPROVEMENTS.md)。

### 文档

- [安装指南](./INSTALLATION_GUIDE.md) - 完整安装说明
- [安全改进](./SECURITY_IMPROVEMENTS.md) - 安全加固详情
- [安全检查清单](./SECURITY_CHECKLIST.md) - 部署和维护指南
- [更新日志](./CHANGELOG.md) - 版本历史

### 测试

```bash
# 运行安全测试
python tests/test_security_improvements.py

# 运行所有测试（如果配置了 pytest）
pytest tests/
```

### 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解贡献指南。

### 安全问题

如发现安全漏洞，请私下联系维护者，不要公开提交 issue。

### 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](./LICENSE) 文件。

---

## Acknowledgments

- Built for the [Codex](https://github.com/openai/codex) ecosystem
- Compatible with Model Context Protocol (MCP)

## Support

- 🐛 [Report bugs](https://github.com/yourusername/china-email-plugin/issues)
- 💡 [Request features](https://github.com/yourusername/china-email-plugin/issues)
- 📖 [Read documentation](./INSTALLATION_GUIDE.md)
=======
# 国内 Codex 插件市场

这个仓库是一个本地 Codex 插件市场。入口文件是：

- `.agents/plugins/marketplace.json`

当前已接入插件：

- `china-email`：国内邮箱插件，支持 QQ 邮箱、网易 163/126/yeah、腾讯企业邮箱、阿里企业邮箱、139 邮箱和自定义 IMAP/SMTP 邮箱。

## 在 Codex 中使用

在 Codex App 中打开这个仓库后，插件市场会读取 `.agents/plugins/marketplace.json`，并展示 `国内插件市场` 下的 `国内邮箱` 插件。

安装后，推荐直接让 Codex 打开本地配置向导：

```text
打开国内邮箱配置向导
```

向导会在本机浏览器打开，用户选择邮箱服务商，填写邮箱地址和授权码，然后点保存即可，不需要手动改 JSON。

也可以手动配置：

```bash
mkdir -p ~/.china-email
cp ./plugins/china-email/config/accounts.example.json ~/.china-email/accounts.json
```

编辑 `~/.china-email/accounts.json`，填入邮箱地址、账号名和客户端授权码。

不要使用网页登录密码；QQ、网易等邮箱通常需要先在网页端设置里开启 IMAP/SMTP，并生成授权码或客户端专用密码。

## 从 GitHub 安装

把这个仓库发布到 GitHub 后，其他用户在 Codex App 中打开或克隆该仓库即可看到这个本地插件市场。
如果要进入官方公共插件市场，还需要按官方发布流程提交审核；本仓库已经具备本地 marketplace 结构。

本仓库只提交插件源码和示例配置，不包含任何真实邮箱账号、授权码或本机缓存。真实账号配置会保存在使用者自己的 `~/.china-email/accounts.json`。
>>>>>>> a1e0c22009d87de4f11beac03f1957ed297fe119
