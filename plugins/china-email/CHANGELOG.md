# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Removed the stale nested plugin copy and source backup; the root marketplace now has one plugin source.
- Resolved committed merge-conflict markers and preserved both copyright notices.
- Corrected installation instructions, documentation links, and manifest version alignment.
- Made security tests portable and discoverable by unittest (7 tests total).

## [1.0.0] - 2026-09-21

### Added
- Initial release of China Email MCP plugin
- Support for major Chinese email providers:
  - QQ Mail (smtp.qq.com / imap.qq.com)
  - NetEase Mail (smtp.163.com / imap.163.com)
  - 139 Mail (smtp.139.com / imap.139.com)
  - Aliyun Mail (smtp.aliyun.com / imap.aliyun.com)
  - Tencent Corporate Mail (smtp.exmail.qq.com / imap.exmail.qq.com)
- Email operations:
  - Search emails with IMAP SEARCH queries
  - Read email content (HTML and plain text)
  - Download attachments with batch support
  - Create email drafts
  - Send emails with double confirmation
- Local web-based setup wizard (http://127.0.0.1:8765)
- Multi-account management
- Special handling for NetEase IMAP ID requirements

### Security
- Comprehensive security hardening:
  - Path traversal protection with whitelist validation
  - Attachment size limits (50MB per file, 100MB total)
  - Strict filename sanitization
  - Mailbox name injection prevention
  - Control character validation
  - Error message sanitization (DEBUG_MODE controlled)
  - HTML injection protection with proper escaping
  - CSRF token format validation
  - Email content length validation
- SSL/TLS encrypted connections (IMAP4_SSL, SMTP_SSL)
- Secure credential storage with 0600 file permissions
- Email address masking in responses
- Double confirmation for sending emails (dry_run + confirm_send)

### Documentation
- Complete installation and configuration guide
- Security improvements documentation
- Security checklist for deployment and maintenance
- Comprehensive test suite for security features

### Testing
- Security test suite with 100% pass rate
- Path traversal attack prevention tests
- Filename injection prevention tests
- Mailbox name injection prevention tests
- Send safety mechanism tests
