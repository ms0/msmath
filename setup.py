from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here/"README.md").open(encoding="utf-8").read();

setup(
  name = "msmath",
  version="1.0.18",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/ms0/msmath",
  author="Mike Speciner",
  author_email="ms@alum.mit.edu",
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering :: Mathematics",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
  ],
  package_dir={"":"src"},
  packages=find_packages(where="src"),
  project_urls={
    "Bug Reports" : "https://github.com/ms0/msmath/issues",
    "Source" : "https://github.com/ms0/msmath",
  }
)

