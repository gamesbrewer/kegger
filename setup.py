import os
import ez_setup

ez_setup.use_setuptools()
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Kegger",
    version = "0.4.3",
    author = "Jonathan Ho",
    author_email = "sabahgamemaker@gmail.com",
    description = ("Framework for Flask on GAE aka Kegger because a Keg is like a bunch of Flask"),
    license = "Common Creative 1.0",
    keywords = "Framework GoogleAppEngine Flask",
    url = "http://www.gamesbrewer.com/kegger",
    packages=find_packages(),
    scripts=['kegger/kegger.py'],
    include_package_data=True,
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 0.4.3 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Common Creative 1.0",
    ],
)