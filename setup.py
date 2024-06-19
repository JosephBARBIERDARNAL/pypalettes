from setuptools import setup, find_packages

setup(
    name="pypalettes",
    version="0.0.1",
    packages=find_packages(),
    description="A large collection of color maps for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/pypalettes/blob/main/README.md",
    include_package_data=True,
    package_data={
        'pypalettes': ['palettes.csv'],
    },
    install_requires=[
        "pandas",
        "matplotlib"
    ],
)