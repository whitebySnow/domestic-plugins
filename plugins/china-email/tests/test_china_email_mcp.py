from __future__ import annotations

import importlib.util
import pathlib
import unittest
from email.message import EmailMessage
from unittest import mock


MODULE_PATH = pathlib.Path(__file__).parents[1] / "src" / "china_email_mcp.py"
SPEC = importlib.util.spec_from_file_location("china_email_mcp", MODULE_PATH)
assert SPEC and SPEC.loader
china_email_mcp = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(china_email_mcp)


class SendSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.account = {
            "name": "test",
            "provider": "qq",
            "email": "test@example.com",
            "username": "test@example.com",
            "password": "unused",
            "imap": {"host": "imap.example.com", "port": 993, "secure": True},
            "smtp": {"host": "smtp.example.com", "port": 465, "secure": True},
        }
        self.message = EmailMessage()
        self.preview = {"to": ["recipient@example.com"], "subject": "Test"}

    def test_send_tool_defaults_to_dry_run(self) -> None:
        schema = china_email_mcp.TOOLS["china_email_send_email"]["inputSchema"]
        self.assertTrue(schema["properties"]["dry_run"]["default"])
        self.assertFalse(schema["properties"]["confirm_send"]["default"])

    def test_real_send_requires_second_confirmation(self) -> None:
        with (
            mock.patch.object(china_email_mcp, "resolve_account", return_value=self.account),
            mock.patch.object(
                china_email_mcp,
                "compose_email_message",
                return_value=(self.message, self.preview, ["recipient@example.com"]),
            ),
            mock.patch.object(china_email_mcp, "connect_smtp") as connect_smtp,
        ):
            with self.assertRaisesRegex(china_email_mcp.ToolError, "confirm_send=true"):
                china_email_mcp.send_email(
                    {
                        "to": "recipient@example.com",
                        "subject": "Test",
                        "text": "Body",
                        "dry_run": False,
                    }
                )
            connect_smtp.assert_not_called()


if __name__ == "__main__":
    unittest.main()
