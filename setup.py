from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [
    x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")
]

setup(
  name='trivialaugment',    # This is the name of your PyPI-package.
  version='1.0',            # Update the version number for new releases
  install_requires=install_requires,
  dependency_links=dependency_links
)
