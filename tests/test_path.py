from nose.tools import raises

from path import Path, InsecurePathError

def test_repr():
    p = Path("/temp/test_dir")
    print repr(p)
    assert repr(p) == "Path('/temp/test_dir')"


def test_abs_child():
    p = Path("/tmp/test_dir")
    c = p.child("child_dir")
    assert c.startswith("/tmp/test_dir")
    assert c != p
    assert c is not p


def test_rel_child():
    p = Path("tmp/test_dir")
    c = p.child("child_dir")
    assert c.startswith("tmp/test_dir")
    assert c != p
    assert c is not p


@raises(InsecurePathError)
def test_non_child():
    p = Path("tmp/test_dir")
    c = p.child("../non_child_dir")
    
