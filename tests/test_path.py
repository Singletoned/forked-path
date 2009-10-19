from nose.tools import raises

from path import Path, InsecurePathError


def test_repr():
    p = Path("/temp/test_dir")
    print repr(p)
    assert repr(p) == "Path('/temp/test_dir')"

def test__add():
    p = Path("/tmp/test_dir")
    r = p + "sub_dir"
    assert r == "/tmp/test_dirsub_dir"
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = Path("/tmp/test_dir/")
    r = p + "sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = Path("/tmp/test_dir/")
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir//sub_dir"

def test__radd():
    p = Path("sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dirsub_dir"
    p = Path("/sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = Path("sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = Path("/sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir//sub_dir"

def test_cwd():
    # TODO
    pass

def test_abspath():
    # Check that abspath converts to Path
    p = Path("/tmp/../tmp/test_dir")
    r = p.abspath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, Path)

def test_normcase():
    # TODO
    pass

def test_normpath():
    # Check that normpath runs and converts to Path
    p = Path("/tmp/..//tmp/test_dir")
    r = p.normpath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, Path)

def test_realpath():
    # TODO
    pass

def test_expanduser():
    # Check that expanduser runs and converts to Path
    p = Path("/tmp")
    r = p.expanduser()
    assert r == p
    assert isinstance(r, Path)
    # TODO: Check that it expands `~` properly

def test_expandvars():
    # TODO
    pass

def test_expand():
    # TODO
    pass

def test_get_namebase():
    # Test that _get_namebase doesn't return a path
    p = Path("/tmp/test_file")
    r = p._get_namebase()
    assert r == "test_file"
    assert not isinstance(r, Path)
    p = Path("/tmp/test.file")
    r = p._get_namebase()
    assert r == "test"
    assert not isinstance(r, Path)

def test_get_ext():
    # Test that _get_ext doesn't return a path
    p = Path("/tmp/test_file")
    r = p._get_ext()
    assert r == ""
    assert not isinstance(r, Path)
    p = Path("/tmp/test.file")
    r = p._get_ext()
    assert r == ".file"
    assert not isinstance(r, Path)

def test_abs_child():
    p = Path("/tmp/test_dir")
    r = p.child("child_dir")
    assert r.startswith("/tmp/test_dir")
    assert r != p
    assert r is not p

def test_rel_child():
    p = Path("tmp/test_dir")
    r = p.child("child_dir")
    assert r.startswith("tmp/test_dir")
    assert r != p
    assert r is not p

@raises(InsecurePathError)
def test_non_child():
    p = Path("tmp/test_dir")
    r = p.child("../non_child_dir")
    
