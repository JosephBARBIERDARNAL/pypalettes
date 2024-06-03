from setuptools import setup, find_packages

setup(
    name="pypalettes",
    version="0.0.1",
    packages=find_packages(),
    description="A large collection of matplotlib color maps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="http://www.barberjoseph.com",
    include_package_data=True,
    package_data={
        'pypalettes': ['palettes.csv'],
    },
    install_requires=[
        "pandas",
        "matplotlib"
    ],
)