# simple test - first_test.py

import pytest
# from convertnum.py import convertnum

def f():
    raise SystemExit(1)

def test_first():
    with pytest.raises(SystemExit):
        f()