import setuptools

with open("README.md", "r", encoding="utf-8") as fh
  long_description = fh.read()

setuptools.setup(
  name = "pychart",
  version = "1.0.2",
  author = "ArtificialVoid",
  description = "a package for reading .chart files",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/ArtificialVoid1/Pychart",
  classifiers = [
    "Programming Language :: Python :: 3",
    "Licence :: None",
    "Operating System :: OS Independant"
  ],
  package_dir = {"":"src"},
  packages = setuptools.find_packages(where="src"),
  python_requires = ">=3.6"
)
