# -*- coding: utf-8 -*-

import sys

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
    with path.create_temp_file(count=2, content="foo") as (f_name_1, f_name_2):
        assert f_name_1.exists()
        assert f_name_1.isfile()
        assert f_name_1.text() == "foo"
        assert f_name_2.exists()
        assert f_name_2.isfile()
        assert f_name_2.text() == "foo"
    assert not f_name_1.exists()
    assert not f_name_2.exists()


def test_create_temp_dir():
    with path.create_temp_dir() as temp_dir_name:
        for file_name in ['a', 'b', 'c']:
            len(temp_dir_name.files()) == 0
            temp_dir_name.child(file_name).touch()
        assert len(temp_dir_name.files()) == 3
    assert not temp_dir_name.exists()


def test_temp_sys_argv():
    orig_sys_argv = sys.argv
    with path.temp_sys_argv("foo", "bar"):
        assert sys.argv == ("foo", "bar")
    assert sys.argv != ["foo", "bar"]
    assert sys.argv == orig_sys_argv
