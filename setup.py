import os

from setuptools import setup
#from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'SQLAlchemy',
    'zope.interface',  # Used by zope.sqlalchemy
    'zope.sqlalchemy'
    ]

tests_require = [
    "transaction",
    "pyramid",
    "nose",
    "coverage",
    ]

entry_points = """
"""

setup(name='SQLAHelper',
      version='2.0',
      description='A place for your SQLAlchemy engines, sessions, and bases.',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        ],
      keywords='',
      author="Mike Orr",
      author_email="sluggoster@gmail.com",
      maintainer='Atsushi Odagiri',
      maintainer_email='aodagx@gmail.com',
      url="https://github.com/Pyramid/SQLAHelper",
      license="MIT",
      py_modules=["sqlahelper"],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      extras_require={
        'testing': tests_require,
      },
      install_requires = requires,
      test_suite="sqlahelper",
      entry_points=entry_points,
      )

