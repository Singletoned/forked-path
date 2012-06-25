# -*- coding: utf-8 -*-

import path

def test_temp_path():
    f = path.temp_file()
    assert f.exists()
    assert f.isfile()

def test_temp_dir():
    f = path.temp_dir()
    assert f.exists()
    assert f.isdir()
    f.child('foo').touch()
    assert f.child('foo').exists()

def test_create_temp_file():
    with path.create_temp_file(count=2, content="foo") as (filename_1, filename_2):
        assert filename_1.exists()
        assert filename_1.isfile()
        assert filename_1.text() == "foo"
        assert filename_2.exists()
        assert filename_2.isfile()
        assert filename_2.text() == "foo"
    assert not filename_1.exists()
    assert not filename_2.exists()
