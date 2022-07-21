import unittest

from string_to_markdown_id import convertToMarkdownId


class StringToMarkdownIdTestCase(unittest.TestCase):
    """Example tests"""

    def testExampleList(self) -> None:
        """Check custom example if sctipt works"""
        testQueries = [
            r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t""",
            "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t",
        ]
        expected = [
            "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t",
            "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t-1",
        ]

        gens = convertToMarkdownId(testQueries)

        self.assertTrue(gens == expected, f"{gens} != {expected}")
        self.assertIsInstance(gens, list)

    def testExampleString(self) -> None:
        """Check custom example if sctipt works"""
        testQuery = r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t"""
        expected = "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t"

        gens = convertToMarkdownId(testQuery)

        self.assertTrue(gens == expected, f"{gens} != {expected}")
        self.assertIsInstance(gens, str)

    def testExampleListHyphenIgnore(self) -> None:
        """Check custom example if sctipt works"""
        testQueries = [
            r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t""",
            "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t",
        ]
        expected = [
            "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t",
            "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t-1",
        ]

        gens = convertToMarkdownId(testQueries, ignore_multi_hyphens=True)

        self.assertTrue(gens == expected, f"{gens} != {expected}")
        self.assertIsInstance(gens, list)

    def testExampleStringHyphenIgnore(self) -> None:
        """Check custom example if sctipt works"""
        testQuery = r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t"""
        expected = "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t"

        gens = convertToMarkdownId(testQuery, ignore_multi_hyphens=True)

        self.assertTrue(gens == expected, f"{gens} != {expected}")
        self.assertIsInstance(gens, str)


if __name__ == "__main__":
    unittest.main()
