try:
    import py
except ImportError:
    py = None

from path import path, InsecurePathError

def test_repr():
    p = path("/temp/test_dir")
    assert repr(p) == "path('/temp/test_dir')"

def test__add():
    p = path("/tmp/test_dir")
    r = p + "sub_dir"
    assert r == "/tmp/test_dirsub_dir"
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = path("/tmp/test_dir/")
    r = p + "sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = path("/tmp/test_dir/")
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir//sub_dir"

def test__radd():
    p = path("sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dirsub_dir"
    p = path("/sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = path("sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = path("/sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir//sub_dir"

def test_cwd():
    # TODO
    pass

def test_abspath():
    # Check that abspath converts to path
    p = path("/tmp/../tmp/test_dir")
    r = p.abspath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, path)

def test_normcase():
    # TODO
    pass

def test_normpath():
    # Check that normpath runs and converts to path
    p = path("/tmp/..//tmp/test_dir")
    r = p.normpath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, path)

def test_realpath():
    # TODO
    pass

def test_expanduser():
    # Check that expanduser runs and converts to path
    p = path("/tmp")
    r = p.expanduser()
    assert r == p
    assert isinstance(r, path)
    # TODO: Check that it expands `~` properly

def test_expandvars():
    # TODO
    pass

def test_expand():
    # TODO
    pass

def test_get_namebase():
    # Test that _get_namebase doesn't return a path
    p = path("/tmp/test_file")
    r = p._get_namebase()
    assert r == "test_file"
    assert not isinstance(r, path)
    p = path("/tmp/test.file")
    r = p._get_namebase()
    assert r == "test"
    assert not isinstance(r, path)

def test_get_ext():
    # Test that _get_ext doesn't return a path
    p = path("/tmp/test_file")
    r = p._get_ext()
    assert r == ""
    assert not isinstance(r, path)
    p = path("/tmp/test.file")
    r = p._get_ext()
    assert r == ".file"
    assert not isinstance(r, path)

def test_parent():
    # Test that parent returns the previous dir
    p = path("/tmp/sub_dir")
    r = p.parent
    assert r == "/tmp"
    assert isinstance(r, path)

def test_abs_child():
    p = path("/tmp/test_dir")
    r = p.child("child_dir")
    assert r == "/tmp/test_dir/child_dir"
    assert r.startswith("/tmp/test_dir")
    assert r != p
    assert r is not p

def test_rel_child():
    p = path("tmp/test_dir")
    r = p.child("child_dir")
    assert r == "tmp/test_dir/child_dir"
    assert r.startswith("tmp/test_dir")
    assert r != p
    assert r is not p

if py:
    def test_non_child():
        def do_test():
            p = path("tmp/test_dir")
            r = p.child("../non_child_dir")

        py.test.raises(InsecurePathError, do_test)
