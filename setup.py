from setuptools import setup, find_packages

setup(
    name="purrpalette",
    version="0.0.1",
    packages=find_packages(),
    description="A large collection of matplotlib color maps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="http://www.barberjoseph.com",
    install_requires=[
        "pandas",
        "matplotlib"
    ],
)