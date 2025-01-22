from setuptools import setup

setup(
    name="pypalettes",
    version="0.1.5",
    packages=["pypalettes"],
    description="A large (+2500) collection of color maps for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/pypalettes/blob/main/README.md",
    include_package_data=True,
    package_data={
        "pypalettes": ["palettes.csv"],
    },
    install_requires=["matplotlib>=3.10.0"],
)
