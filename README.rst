A fork of Jason Orendorff's excellent path.py.  With the intention of
giving it greater availabilty, tests, documentation and also bringing
in some of the simpler parts of twisted.python.filepath.

Usage::

    >>> from path import Path
    >>> tmp_dir = Path('/tmp/')
    >>> tmp_dir
    Path('/tmp/')
    >>> tmp_dir_existed = tmp_dir.exists()
    >>> tmp_dir == '/tmp/'
    True
    >>> sub_dir = tmp_dir + 'sub_dir/'
    >>> sub_dir
    Path('/tmp/sub_dir/')
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


