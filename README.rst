String to Markdown Id
#####################

Convert string to GitLab Flavored Markdown Header ID `[1] <https://docs.gitlab.com/ee/user/markdown.html#header-ids-and-links>`_


Quickstart
==========

String to Markdown Id is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install string_to_markdown_id

After installing String to Markdown Id you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    from string_to_markdown_id import convertToMarkdownId

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

    gens = convertToMarkdownId(testQueries, ignore_multi_hyphens=True)
    print(f"Generated IDs (Hyphen Ignored):\n{gens}\n")

    print(f"Expected IDs (Hyphen Ignored):\n{expectedHyphenIgnore}\n")

The `API Reference <http://string_to_markdown_id.readthedocs.io>`_ provides API-level documentation.
