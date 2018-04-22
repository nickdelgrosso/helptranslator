import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "helptranslator",
    version = "0.0.1",
    author = "Nicholas A. Del Grosso",
    author_email = "delgrosso.nick@gmail.com",
    description = ("A Python module that uses Google Translate to automatically translate Python help text to any language."),
    license = "BSD",
    keywords = "translate help python",
    install_requires = ['googletrans'],
    py_modules = ['helptranslator'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
