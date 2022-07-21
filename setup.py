import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r".*__version__ = [\'\"](.*?)[\'\"]", re.S)

base_package = "string_to_markdown_id"
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, "src", "string_to_markdown_id", "__init__.py")
with open(init_file, "r", encoding="utf-8") as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(f"Cannot find __version__ in {init_file}")

with open("README.rst", "r", encoding="utf-8") as f:
    readme = f.read()

with open("CHANGELOG.rst", "r", encoding="utf-8") as f:
    changes = f.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file"""
    with open(filename, "r", encoding="utf-8") as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


requirements = parse_requirements("requirements.txt")


if __name__ == "__main__":
    setup(
        name="string_to_markdown_id",
        description="Convert string to GitLab Flavored Markdown Header ID",
        long_description="\n\n".join([readme, changes]),
        license="MIT license",
        url="https://github.com/PROxZIMA/string_to_markdown_id",
        version=version,
        author="PROxZIMA",
        author_email="contact@proxzima.dev",
        maintainer="PROxZIMA",
        maintainer_email="contact@proxzima.dev",
        install_requires=requirements,
        keywords=["string_to_markdown_id"],
        package_dir={"": "src"},
        packages=find_packages("src"),
        zip_safe=False,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )
