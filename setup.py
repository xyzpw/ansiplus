import setuptools
import ansiplus

def getReadme():
    with open("README.md", 'r') as f:
        return f.read()

setuptools.setup(
    name="ansiplus",
    author=ansiplus.__author__,
    maintainer=ansiplus.__author__,
    version=ansiplus.__version__,
    description=ansiplus.__description__,
    url="https://github.com/xyzpw/ansiplus/",
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
    license=ansiplus.__license__,
)
