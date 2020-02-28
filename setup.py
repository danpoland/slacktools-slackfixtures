#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="slacktools-slackfixtures",
    version="1.0.0",
    author="Daniel Poland",
    author_email="dan@crispy.dev",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danpoland/slacktools-slackfixtures",
    py_modules=["pytest_slackfixtures"],
    install_requires=["pytest~=5.3.5", "pytest-mock~=2.0.0", "slackclient~=2.5.0"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Pytest",
    ],
    entry_points={"pytest11": ["slackfixtures = pytest_slackfixtures"]},
)
