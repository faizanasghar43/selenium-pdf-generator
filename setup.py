from setuptools import setup, find_packages

setup(
    name="selenium-pdf-generator",
    version="0.1.0",
    description="Generate PDF files from any URL using Selenium and Chrome",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Faizan Asghar",
    author_email="faizandev43@outlook.com",
    url="https://github.com/faizanasghar43/selenium-pdf-generator",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "webdriver-manager>=3.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
