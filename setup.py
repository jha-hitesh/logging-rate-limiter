"""Library Metadata Information."""

from setuptools import find_packages
from setuptools import setup

description = ("rate limiting filter for python logging module.")

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements():
    """Get Requirement."""
    with open("requirements.txt") as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


setup(
    name="logging_rate_limiter",
    version="1.0.0",
    author="hitesh jha",
    author_email="hitesh4official@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jha-hitesh/logging-rate-limiter",
    packages=["logging_rate_limiter"],
    license="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=get_requirements(),
    python_requires=">=3.6",
)
