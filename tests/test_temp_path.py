# -*- coding: utf-8 -*-

import path

def test_temp_path():
    f = path.temp_file()
    assert f.exists()
    assert f.isfile()

