import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ToolTests(unittest.TestCase):
    def test_port_parser(self):
        module = load_tool("tcp_inventory")
        self.assertEqual(module.parse_ports("22,80,443,80"), [22, 80, 443])
        with self.assertRaises(Exception):
            module.parse_ports("0")
        with self.assertRaises(Exception):
            module.parse_ports("70000")

    def test_config_rules_redact_values(self):
        module = load_tool("config_audit")
        sample = "DEBUG=true"
        matches = [rule for rule in module.RULES if rule[1].search(sample)]
        self.assertEqual(matches[0][0], "DEBUG_TRUE")
        self.assertNotIn("true", "DEBUG=<redacted>")


if __name__ == "__main__":
    unittest.main()
