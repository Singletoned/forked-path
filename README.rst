A fork of Jason Orendorff's excellent path.py.  With the intention of
giving it greater availabilty, tests, documentation and also bringing
in some of the simpler parts of twisted.python.filepath.

This module provides a subsclass of string (or unicode) with utility
methods that provide easy access to most of os.path, and the relevant
parts of os.

Usage::

    >>> from path import path
    >>> tmp_dir = path('/tmp/')
    >>> tmp_dir
    path('/tmp/')
    >>> tmp_dir_existed = tmp_dir.exists()
    >>> tmp_dir == '/tmp/'
    True
    >>> sub_dir = tmp_dir + 'sub_dir/'
    >>> sub_dir
    path('/tmp/sub_dir/')
    >>> sub_dir.makedirs()
    >>> file1 = sub_dir + 'file1.txt'
    >>> file1.touch()
    >>> file2 = sub_dir + 'file2.txt'
    >>> file2.touch()
    >>> for f in sub_dir.files():
    ...     print f
    ... 
    /tmp/sub_dir/file1.txt
    /tmp/sub_dir/file2.txt
    >>> for f in sub_dir.files():
    ...    f.remove()
    ... 
    >>> sub_dir.files()
    []
    >>> sub_dir.rmdir()
    >>> sub_dir.exists()
    False
    >>> if not tmp_dir_existed:
    ...     tmp_dir.rmdir()
    ... 


This module should be as stable as the last release of path.py (2.2),
and I am gradually adding regression tests to ensure that compatabilty
is kept going forward.  However this module itself isn't being used in
production yet, and hasn't been tested thoroughly on Windows, so some
caution should be taken for now.

I'm happy to take any suggestions, criticism, advice or comments.  For
now, email me at singletoned@gmail.com or use the messages on github.
