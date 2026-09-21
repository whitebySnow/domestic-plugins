# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

### Reporting Process

1. **Email the maintainer privately** with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

2. **Wait for acknowledgment** (typically within 48 hours)

3. **Coordinate disclosure timeline**:
   - We aim to fix critical vulnerabilities within 7 days
   - High-severity issues within 30 days
   - Medium/low-severity issues within 90 days

4. **Public disclosure**:
   - After a fix is released, we will:
     - Publish a security advisory
     - Credit the reporter (unless they prefer anonymity)
     - Update CHANGELOG.md

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial assessment**: Within 7 days
- **Status updates**: Every 7-14 days until resolved
- **Credit**: Public acknowledgment in security advisory (optional)

## Security Measures

This plugin implements multiple layers of security:

### 1. Input Validation
- All user inputs are validated and sanitized
- Path traversal prevention
- Filename sanitization
- Mailbox name validation
- Email content length limits

### 2. Resource Limits
- Attachment size: 50MB per file
- Total attachment size: 100MB per operation
- Email recipients: Maximum 100 per message
- Subject line: 998 characters
- Email body: 10MB

### 3. Credential Protection
- Configuration stored with 0600 permissions
- No plaintext passwords in logs
- Email addresses masked in output
- SSL/TLS for all network connections

### 4. Safe Defaults
- Email sending requires double confirmation
- `dry_run=True` by default
- Debug mode disabled in production
- Error messages sanitized

### 5. Network Security
- IMAP: SSL/TLS (port 993)
- SMTP: SSL/TLS (port 465)
- Certificate verification enabled
- No fallback to insecure connections

## Known Security Considerations

### 1. Authorization Codes
Users must obtain app-specific passwords from email providers. These are stored locally in `~/.china-email/accounts.json` with restricted permissions (0600).

**Best practices**:
- Never commit `accounts.json` to version control
- Rotate authorization codes periodically
- Revoke unused authorization codes

### 2. Attachment Storage
Downloaded attachments are stored in `~/.china-email/attachments/` by default.

**Best practices**:
- Regularly clean up old attachments
- Scan attachments with antivirus software
- Be cautious with executable files

### 3. Local Web Server
The setup wizard runs a local HTTP server on `127.0.0.1:8765`.

**Security features**:
- Listens only on localhost
- CSRF token with 60-second TTL
- Automatic timeout after 10 minutes
- No external access

### 4. Debug Mode
When `DEBUG_MODE=1`, detailed error messages including stack traces are shown.

**Best practices**:
- Never enable in production
- Disable after troubleshooting
- Check logs for sensitive information before sharing

## Security Audit History

### v1.0.0 (2026-09-21)
- Initial security audit completed
- 8 major security improvements implemented
- All tests passing

## Security Testing

Run security tests:

```bash
python tests/test_security_improvements.py
```

Expected output:
```
[PASS] Security constants defined
[PASS] validate_safe_path function exists and works
[PASS] Enhanced format_mailbox_arg with security checks
[PASS] Enhanced sanitize_filename with strict validation
[PASS] Send safety defaults maintained

ALL SECURITY TESTS PASSED
```

## Dependency Security

Check for vulnerable dependencies:

```bash
pip install pip-audit
pip-audit
```

Update dependencies:

```bash
pip install -U -r requirements.txt
```

## Security Checklist

Before deployment:
- [ ] `DEBUG_MODE` is disabled
- [ ] File permissions verified (0600 for accounts.json)
- [ ] Dependencies up to date
- [ ] Security tests passing
- [ ] No secrets in version control

During operation:
- [ ] Monitor logs for security warnings
- [ ] Regularly clean up attachments
- [ ] Update dependencies monthly
- [ ] Review authorization codes quarterly

## Additional Resources

- [SECURITY_IMPROVEMENTS.md](./SECURITY_IMPROVEMENTS.md) - Detailed security features
- [SECURITY_CHECKLIST.md](./SECURITY_CHECKLIST.md) - Operational security guide

## Hall of Fame

Security researchers who have responsibly disclosed vulnerabilities:

_(None yet - be the first!)_

---

**Last Updated**: 2026-09-21  
**Next Review**: 2027-03-21
