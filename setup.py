# bumpversion --current-version <__version__> (major|minor|patch) setup.py

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="imgen",
    version="0.1.1",
    description="Image generator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zahash/imgen",
    author="zahash",
    author_email="zahash.z@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["imgen"],
    include_package_data=True,
    install_requires=requirements,
)
