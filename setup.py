from setuptools import setup, find_packages

version = '0.2.3'

setup(
    name='forked-path',
    version=version,
    author="Ed Singleton",
    author_email="singletoned@gmail.com",
    description="An object oriented file path module",
    url="http://github.com/Singletoned/forked-path",
    long_description="""A fork of path.py by Jason Orendorff.  Regression tests and small enhancements by Ed Singleton.
""",
    classifiers=[
        "Programming Language :: Python",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
    ],
    keywords='path path.py file',
    license='',
    py_modules=['path'],
    include_package_data=True,
    zip_safe=False,
)
