from setuptools import setup

version = '0.3'

setup_data = dict(
    name='forked-path',
    version=version,
    author="Ed Singleton",
    author_email="singletoned@gmail.com",
    description="An object oriented file path module",
    url="http://github.com/Singletoned/forked-path",
    long_description="""
        A fork of path.py by Jason Orendorff.
        Regression tests and small enhancements by Ed Singleton.
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
    install_requires=[
        'six',
    ],
    py_modules=['path'],
    include_package_data=True,
    zip_safe=False,
)


def main():
    setup(**setup_data)


if __name__ == '__main__':
    main()
