import setuptools
from ansiplus import __version__, __author__, __description__

def getReadme():
    with open("README.md", 'r') as f:
        return f.read()

setuptools.setup(
    name="ansiplus",
    author=__author__,
    maintainer=__author__,
    version=__version__,
    description=__description__,
    python_required=">= 3.10",
    long_description=getReadme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=["ansi", "cursor", "style", "color"],
    license="MIT",
)
