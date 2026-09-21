#!/usr/bin/env python3
"""Security validation tests for improved china_email_mcp.py"""

import pathlib
import sys
import os

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add the plugin src directory to path
plugin_dir = pathlib.Path(r'D:\研究生\图像水印每周报告\domestic-plugins\plugins\china-email\src')
sys.path.insert(0, str(plugin_dir))

def test_security_constants():
    """Test that security constants are defined"""
    import china_email_mcp
    
    assert hasattr(china_email_mcp, 'MAX_ATTACHMENT_SIZE'), "MAX_ATTACHMENT_SIZE not defined"
    assert hasattr(china_email_mcp, 'MAX_TOTAL_ATTACHMENT_SIZE'), "MAX_TOTAL_ATTACHMENT_SIZE not defined"
    assert hasattr(china_email_mcp, 'DEBUG_MODE'), "DEBUG_MODE not defined"
    
    print("[PASS] Security constants defined")
    print(f"  - MAX_ATTACHMENT_SIZE: {china_email_mcp.MAX_ATTACHMENT_SIZE / 1024 / 1024}MB")
    print(f"  - MAX_TOTAL_ATTACHMENT_SIZE: {china_email_mcp.MAX_TOTAL_ATTACHMENT_SIZE / 1024 / 1024}MB")
    print(f"  - DEBUG_MODE: {china_email_mcp.DEBUG_MODE}")

def test_validate_safe_path():
    """Test path validation function"""
    import china_email_mcp
    
    assert hasattr(china_email_mcp, 'validate_safe_path'), "validate_safe_path not defined"
    
    # Test valid path
    home = pathlib.Path.home()
    safe_path = home / "test"
    result = china_email_mcp.validate_safe_path(safe_path, home)
    assert result.is_absolute()
    print("[PASS] validate_safe_path function exists and works")

def test_enhanced_format_mailbox():
    """Test enhanced mailbox name validation"""
    import china_email_mcp
    
    # Test valid names
    assert china_email_mcp.format_mailbox_arg("INBOX") == "INBOX"
    
    # Test that control characters raise error
    try:
        china_email_mcp.format_mailbox_arg("test\x00malicious")
        assert False, "Should raise error for null bytes"
    except china_email_mcp.ToolError as e:
        assert "control characters" in str(e) or "null bytes" in str(e)
    
    print("[PASS] Enhanced format_mailbox_arg with security checks")

def test_enhanced_sanitize_filename():
    """Test enhanced filename sanitization"""
    import china_email_mcp
    
    # Test path traversal prevention
    result1 = china_email_mcp.sanitize_filename("../../../etc/passwd")
    assert ".." not in result1
    
    result2 = china_email_mcp.sanitize_filename("path/to/file")
    assert "/" not in result2
    
    result3 = china_email_mcp.sanitize_filename("path\\to\\file")
    assert "\\" not in result3
    
    # Test special characters
    result4 = china_email_mcp.sanitize_filename("file<>:|?*.txt")
    assert "<" not in result4 and ">" not in result4
    
    # Test dot files
    assert china_email_mcp.sanitize_filename(".") == "attachment"
    assert china_email_mcp.sanitize_filename("..") == "attachment"
    
    print("[PASS] Enhanced sanitize_filename with strict validation")

def test_send_safety():
    """Test that send safety is still enforced"""
    import china_email_mcp
    
    schema = china_email_mcp.TOOLS["china_email_send_email"]["inputSchema"]
    assert schema["properties"]["dry_run"]["default"] == True
    assert schema["properties"]["confirm_send"]["default"] == False
    
    print("[PASS] Send safety defaults maintained")

if __name__ == "__main__":
    print("Running security validation tests...\n")
    
    try:
        test_security_constants()
        test_validate_safe_path()
        test_enhanced_format_mailbox()
        test_enhanced_sanitize_filename()
        test_send_safety()
        
        print("\n" + "="*60)
        print("ALL SECURITY TESTS PASSED")
        print("="*60)
        
    except Exception as e:
        print(f"\n[FAIL] Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
