#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="compyte",              # Package name
    version="0.0.1",                # Initial release version
    packages=find_packages(),       # Automatically find and include all packages
    install_requires=[],            # Optional: List dependencies (if any)
    description="A component parser for html",
    long_description=open('README.org').read(),  # Read long description from file
    long_description_content_type='text/x-org',  # Specify Markdown as the format
    url="https://github.com/spynets/compyte",  # GitHub repo or package URL
    author="Alfred Roos",             # Your name
    author_email="alfred@stensatter.se",  # Your contact email
    license="MIT",                  # License type (e.g., MIT)
    classifiers=[                   # Additional metadata about your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',        # Python version compatibility
)
