from setuptools import setup, find_packages

version = '0.1'

setup(name='forked-path',
      version=version,
      author="Ed Singleton",
      author_email="singletoned@gmail.com",
      description="An object oriented file path module",
      url="http://github.com/Singletoned/forked-path",
      long_description="""A fork of path.py by Jason Orendorff.  Regression tests and small enhancements by Ed Singleton.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      license='',
      py_modules=['path'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
