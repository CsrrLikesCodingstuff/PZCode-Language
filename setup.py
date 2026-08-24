[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"

[project]
name = "PZCode" 
version = "1.0.1" 
description = "A custom programming language interpreter"
readme = "README.md"
requires-python = ">=3.12"
license = { text = "MIT" }
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    
]

[project.scripts]
pzcode = "pzcode:main" 
