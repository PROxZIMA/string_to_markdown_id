"""
Convert string to GitLab Flavored Markdown Header ID
"""

__version__ = "0.0.1"

import re
from collections import Counter
from typing import List, Union

__all__ = [
    "convertToMarkdownId",
    "toLowerCase",
    "dropNonWord",
    "replaceSpaceWithHyphen",
    "hyphensManyToOne",
    "manageDuplicates",
]


def convertToRaw(queries: List[str]) -> List[str]:
    """Convert list of query strings to raw strings.

    Args:
        param1: List of strings.

    Returns:
        List of corresponding raw strings.

    """
    return [repr(rf"{query}") for query in queries]


# Rules


def toLowerCase(s: str) -> str:
    """Rule 1. All text is converted to lowercase."""
    return s.lower()


def dropNonWord(s: str) -> str:
    """Rule 2. All non-word text (such as punctuation or HTML except '-' and space ) is removed.

    Replace actual TAB. \t is converted to \\t in raw conversion.
    A sole \t might be there in string because of the TAB unicode in the string.
    """
    s = re.sub(r"(?<!\\)\\t", "", s)
    return re.sub(r"[^\w\s-]", "", s)


def replaceSpaceWithHyphen(s: str) -> str:
    r"""Rule 3. All spaces are converted to hyphens. (space unicode not \s)"""
    return re.sub(r"[ ]", "-", s)


def hyphensManyToOne(s: str) -> str:
    """Rule 4. Two or more hyphens in a row are converted to one.

    Note: Ignored in Github Markdown
    """
    return re.sub(r"-{2,}", "-", s)


def manageDuplicates(generated: List[str]) -> List[str]:
    """Rule 5. If a header with the same ID has already been generated, a unique incrementing number is appended, starting at 1."""
    generatedCounter = Counter(generated)

    for i in range(len(generated) - 1, -1, -1):
        query = generated[i]
        count = generatedCounter[query]
        if count > 1:
            generated[i] += f"-{count - 1}"
            generatedCounter[query] -= 1

    return generated


def convertToMarkdownId(
    queries: Union[List[str], str], ignore_multi_hyphens=False
) -> Union[List[str], str]:
    """Convert list of query strings or a single string to [GLFM Header ID](https://docs.gitlab.com/ee/user/markdown.html#header-ids-and-links)

    Args:
        param1: List of strings or a single string.
        param2: True to ignore [Rule 4](https://docs.gitlab.com/ee/user/markdown.html#header-ids-and-links).

    Returns:
        List of corresponding IDs or a single string ID.

    """
    isString = isinstance(queries, str)
    if isString:
        queries = [queries]

    if not isinstance(queries, list):
        raise TypeError(
            f"Argument must be a list of strings or a single string. Found: {type(queries)}"
        )

    queries = convertToRaw(queries)

    rules = [
        toLowerCase,
        dropNonWord,
        replaceSpaceWithHyphen,
    ]

    if not ignore_multi_hyphens:
        rules.append(hyphensManyToOne)

    for i, _ in enumerate(queries):
        for rule in rules:
            queries[i] = rule(queries[i])

    generated = manageDuplicates(queries)

    return generated[0] if isString else generated


if __name__ == "__main__":
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
