# Contributing to China Email MCP Plugin

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Prioritize the security and privacy of users

## How to Contribute

### Reporting Bugs

Before creating a bug report:
1. Check existing issues to avoid duplicates
2. Collect relevant information (OS, Python version, error messages)
3. Create a minimal reproduction example

**Bug Report Template**:
```markdown
**Description**: Clear description of the bug

**Steps to Reproduce**:
1. Step one
2. Step two
3. ...

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happens

**Environment**:
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python version: [e.g., 3.10.5]
- Plugin version: [e.g., 1.0.0]

**Additional Context**: Any other relevant information
```

### Suggesting Features

Feature suggestions are welcome! Please:
1. Check if the feature has already been requested
2. Clearly describe the use case and benefits
3. Consider backward compatibility
4. Discuss implementation approach if possible

### Pull Requests

1. **Fork and Clone**
   ```bash
   # Clone your fork, then run from its repository root:
   cd plugins/china-email
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-123
   ```

3. **Make Changes**
   - Follow existing code style
   - Add tests for new features
   - Update documentation as needed
   - Keep commits focused and atomic

4. **Test Your Changes**
   ```bash
   # Run security tests
   python tests/test_security_improvements.py
   
   # Run all tests
   python -m unittest discover -s tests -v
   ```

5. **Commit**
   ```bash
   git commit -m "feat: add support for Gmail IMAP"
   # or
   git commit -m "fix: resolve path traversal in attachment download"
   ```

   Use conventional commit messages:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `test:` Test additions or fixes
   - `refactor:` Code refactoring
   - `security:` Security improvements
   - `chore:` Maintenance tasks

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a pull request on GitHub.

### Code Style

- Follow PEP 8 for Python code
- Use type hints for function signatures
- Write docstrings for public functions
- Keep functions focused and small
- Use meaningful variable names

**Example**:
```python
def validate_email_address(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### Testing Guidelines

- Write tests for new features
- Ensure existing tests still pass
- Test edge cases and error conditions
- Use descriptive test names

**Example**:
```python
def test_attachment_size_limit():
    """Test that attachments exceeding size limit are rejected."""
    large_data = b"x" * (51 * 1024 * 1024)  # 51MB
    with pytest.raises(ToolError, match="exceeds size limit"):
        save_large_attachment(large_data)
```

### Security Guidelines

Security is a top priority. When contributing:

- **Never commit secrets**: No passwords, API keys, or tokens
- **Validate all inputs**: Assume all external data is malicious
- **Use parameterized queries**: Prevent injection attacks
- **Sanitize file paths**: Prevent path traversal
- **Limit resource usage**: Prevent DoS attacks
- **Encrypt sensitive data**: Use SSL/TLS for network, proper permissions for files

**Reporting Security Issues**:
- Do NOT open public issues for security vulnerabilities
- Email the maintainer privately with details
- Allow reasonable time for a fix before disclosure

### Documentation

When adding features:
- Update README.md if user-facing
- Add docstrings to functions
- Update CHANGELOG.md
- Include usage examples

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run from plugins/china-email; runtime uses only the standard library.

# Install development dependencies
pip install pytest pytest-cov black flake8
```

### Running Tests

```bash
# Run all tests without extra dependencies
python -m unittest discover -s tests -v

# Run with coverage
pytest --cov=china_email_mcp tests/

# Run specific test file
pytest tests/test_security_improvements.py

# Run with verbose output
pytest -v tests/
```

### Code Review Process

All pull requests will be reviewed for:
- Code quality and style
- Test coverage
- Documentation completeness
- Security implications
- Backward compatibility

Expect feedback and be prepared to make revisions.

## Questions?

Feel free to:
- Open a discussion on GitHub
- Ask in pull request comments
- Email the maintainer

Thank you for contributing! 🎉
