import unittest
from modules.utils import *


class TestStringMethods(unittest.TestCase):

    def test_get_env_or_default_returns_default_value_for_nonexisting_env(self):
        default = "DEFAULT"
        result = get_env_or_default("this env var does not exist", "DEFAULT")
        self.assertEqual(result, default)

    def test_get_env_or_default_returns_env_var(self):
        default = "DEFAULT"
        expected = "EXPECTED_CONTENT"
        var_name = "VARNAME_FOR_TEST"
        os.environ[var_name] = expected
        result = get_env_or_default(var_name, default)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
