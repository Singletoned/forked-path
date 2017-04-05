import io

import nose

import path


def test_repr():
    p = path.path("/temp/test_dir")
    assert repr(p) == "path('/temp/test_dir')"


def test__add():
    p = path.path("/tmp/test_dir")
    r = p + "sub_dir"
    assert r == "/tmp/test_dirsub_dir"
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = path.path("/tmp/test_dir/")
    r = p + "sub_dir"
    assert r == "/tmp/test_dir/sub_dir"
    p = path.path("/tmp/test_dir/")
    r = p + "/sub_dir"
    assert r == "/tmp/test_dir//sub_dir"


def test__radd():
    p = path.path("sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dirsub_dir"
    p = path.path("/sub_dir")
    r = "/tmp/test_dir" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = path.path("sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir/sub_dir"
    p = path.path("/sub_dir")
    r = "/tmp/test_dir/" + p
    assert r == "/tmp/test_dir//sub_dir"


def test_cwd():
    # TODO
    pass


def test_abspath():
    # Check that abspath converts to path.path
    p = path.path("/tmp/../tmp/test_dir")
    r = p.abspath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, path.path)


def test_normcase():
    # TODO
    pass


def test_normpath():
    # Check that normpath runs and converts to path.path
    p = path.path("/tmp/..//tmp/test_dir")
    r = p.normpath()
    assert r == "/tmp/test_dir"
    assert isinstance(r, path.path)


def test_realpath():
    # TODO
    pass


def test_expanduser():
    # Check that expanduser runs and converts to path.path
    p = path.path("/tmp")
    r = p.expanduser()
    assert r == p
    assert isinstance(r, path.path)
    # TODO: Check that it expands `~` properly


def test_expandvars():
    # TODO
    pass


def test_expand():
    # TODO
    pass


def test_get_namebase():
    # Test that _get_namebase doesn't return a path.path
    p = path.path("/tmp/test_file")
    r = p._get_namebase()
    assert r == "test_file"
    assert not isinstance(r, path.path)
    p = path.path("/tmp/test.file")
    r = p._get_namebase()
    assert r == "test"
    assert not isinstance(r, path.path)


def test_get_ext():
    # Test that _get_ext doesn't return a path.path
    p = path.path("/tmp/test_file")
    r = p._get_ext()
    assert r == ""
    assert not isinstance(r, path.path)
    p = path.path("/tmp/test.file")
    r = p._get_ext()
    assert r == ".file"
    assert not isinstance(r, path.path)


def test_parent():
    # Test that parent returns the previous dir
    p = path.path("/tmp/sub_dir")
    r = p.parent
    assert r == "/tmp"
    assert isinstance(r, path.path)


def test_abs_child():
    p = path.path("/tmp/test_dir")
    r = p.child("child_dir")
    assert r == "/tmp/test_dir/child_dir"
    assert r.startswith("/tmp/test_dir")
    assert r != p
    assert r is not p


def test_rel_child():
    p = path.path("tmp/test_dir")
    r = p.child("child_dir")
    assert r == "tmp/test_dir/child_dir"
    assert r.startswith("tmp/test_dir")
    assert r != p
    assert r is not p


@nose.tools.raises(path.InsecurePathError)
def test_non_child():
    p = path.path("tmp/test_dir")
    p.child("../non_child_dir")


def test_hash():
    def mock_open(self):
        return io.BytesIO(b"hello\n")

    m = path.path("/tmp/hullo.txt")
    m.open = mock_open
    h = m.read_md5()
    assert h == b"\xb1\x94j\xc9$\x92\xd24|b5\xb4\xd2a\x11\x84"
