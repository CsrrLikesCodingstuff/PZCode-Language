from setuptools import setup, find_packages

setup(
    name="PZCode-Language",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pzcode=interpreter:main",  # Change this to match your actual main function if needed
        ],
    },
    author="CsrrLikesCodingstuff",
    description="An Easy-2-use Open Source Programming language with an interactive interpreter.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CsrrLikesCodingstuff/PZCode-Language",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
