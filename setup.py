# pylint: disable= missing-docstring
from setuptools import setup, find_packages

setup(name="unittesting",
      version="0.1.0",
      description="learning unit testing",
      author="Pedro J Asensio",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="arun.kr.khattri@gmail.com",
      install_requires=["pandas",
                        "matplotlib",
                        "pytest",
                        "pytest-mpl",
                        "pytest-mock",
                        "scipy",
                        "numpy"],)