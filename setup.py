import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
__version__ = "0.0.1"

REPONAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Shadhil24"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shadhilsirajudheenck@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)