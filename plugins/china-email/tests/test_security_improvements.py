#!/usr/bin/env python3
"""Security validation tests for improved china_email_mcp.py"""

import pathlib
import sys
import unittest

# Resolve the source directory relative to this test, independent of checkout location.
plugin_dir = pathlib.Path(__file__).resolve().parents[1] / "src"
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

def load_tests(loader, tests, pattern):
    return unittest.TestSuite(
        unittest.FunctionTestCase(test)
        for test in (
            test_security_constants,
            test_validate_safe_path,
            test_enhanced_format_mailbox,
            test_enhanced_sanitize_filename,
            test_send_safety,
        )
    )


if __name__ == "__main__":
    unittest.main()
