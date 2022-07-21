import unittest

import string_to_markdown_id


class VersionTestCase(unittest.TestCase):
    """Version tests"""

    def test_version(self):
        """check string_to_markdown_id exposes a version attribute"""
        self.assertTrue(hasattr(string_to_markdown_id, "__version__"))
        self.assertIsInstance(string_to_markdown_id.__version__, str)


if __name__ == "__main__":
    unittest.main()
