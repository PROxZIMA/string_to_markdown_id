"""
This example script imports the string_to_markdown_id package and
prints out the version.
"""

from string_to_markdown_id import __version__, convertToMarkdownId


def main():
    """main function"""
    print(f"string_to_markdown_id version: {__version__}")

    print("List usage ->")

    testQueries = [
        r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t""",
        "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t",
    ]
    expected = [
        "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t",
        "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t-1",
    ]
    expectedHyphenIgnore = [
        "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t",
        "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t-1",
    ]
    print(f"\nGiven queries:\n{testQueries}\n")

    gens = convertToMarkdownId(testQueries)
    print(f"Generated IDs:\n{gens}\n")

    print(f"Expected IDs:\n{expected}\n")
    assert gens == expected, f"{gens} != {expected}"
    assert isinstance(gens, list), f"{gens} is not a list"

    gens = convertToMarkdownId(testQueries, ignore_multi_hyphens=True)
    print(f"Generated IDs (Hyphen Ignored):\n{gens}\n")

    print(f"Expected IDs (Hyphen Ignored):\n{expectedHyphenIgnore}\n")
    assert gens == expectedHyphenIgnore, f"{gens} != {expectedHyphenIgnore}"
    assert isinstance(gens, list), f"{gens} is not a list"

    print("String usage ->")

    testQuery = r"""(This) --- --v - " "" ' ' has 2.5, 😀, 한글, :thumbsup:, 	, \n, \r, \t, \f, \u, \a, \x, \\t"""
    expected = "this-v-has-25-한글-thumbsup-n-r-t-f-u-a-x-t"
    expectedHyphenIgnore = "this-------v-------has-25--한글-thumbsup--n-r-t-f-u-a-x-t"
    print(f"\nGiven query:\n{testQuery}\n")

    gens = convertToMarkdownId(testQuery)
    print(f"Generated ID:\n{gens}\n")

    print(f"Expected ID:\n{expected}\n")
    assert gens == expected, f"{gens} != {expected}"
    assert isinstance(gens, str), f"{gens} is not a string"

    gens = convertToMarkdownId(testQuery, ignore_multi_hyphens=True)
    print(f"Generated ID (Hyphen Ignored):\n{gens}\n")

    print(f"Expected ID (Hyphen Ignored):\n{expectedHyphenIgnore}\n")
    assert gens == expectedHyphenIgnore, f"{gens} != {expectedHyphenIgnore}"
    assert isinstance(gens, str), f"{gens} is not a string"


if __name__ == "__main__":
    main()
