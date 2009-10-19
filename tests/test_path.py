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
    
