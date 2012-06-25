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
