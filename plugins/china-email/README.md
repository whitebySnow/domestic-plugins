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

Run from the repository root. The server uses only the Python standard library; no pip installation is needed.

```bash
cd plugins/china-email
python src/china_email_mcp.py setup
```

The setup wizard saves account settings to `~/.china-email/accounts.json`. Enable IMAP/SMTP at your provider and use a client authorization code. Alternatively, copy `config/accounts.example.json` to that location and edit your own copy.

For an MCP client, configure the command as `python` and its argument as the **absolute path** to `src/china_email_mcp.py`. The plugin's `.mcp.json` uses a path relative to the plugin directory; clients using that file must launch it with the plugin directory as their working directory.

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

See [SECURITY.md](./SECURITY.md) for details.

### Documentation

- [Installation / 安装](#installation)
- [Security / 安全说明](./SECURITY.md)
- [Changelog](./CHANGELOG.md) - Version history

### Testing

```bash
# Run security tests
python tests/test_security_improvements.py

# Run all 7 tests
python -m unittest discover -s tests -v
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

从仓库根目录执行。服务器只使用 Python 标准库，无需安装第三方运行依赖。

```bash
cd plugins/china-email
python src/china_email_mcp.py setup
```

配置向导将账户信息保存到 `~/.china-email/accounts.json`。请先开启邮箱的 IMAP/SMTP，并使用客户端授权码。也可复制 `config/accounts.example.json` 到该位置，再修改自己的配置。

MCP 客户端启动命令使用 `python`，参数使用 `src/china_email_mcp.py` 的绝对路径。插件自带的 `.mcp.json` 使用相对路径，需以插件目录为工作目录。

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

详见 [SECURITY.md](./SECURITY.md)。

### 文档

- [Installation / 安装](#installation)
- [Security / 安全说明](./SECURITY.md)
- [更新日志](./CHANGELOG.md) - 版本历史

### 测试

```bash
# 运行安全测试
python tests/test_security_improvements.py

# 运行全部 7 项测试
python -m unittest discover -s tests -v
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

Report bugs and request features through the repository issue tracker. See [installation instructions](#installation) and [contributing guidelines](./CONTRIBUTING.md).
