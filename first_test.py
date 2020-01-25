# simple test - first_test.py

import pytest
from convertnum import convertnum

def f():
    raise SystemExit(1)

def test_first():
	testinp = [111, 40, 55, 2]
	testout = ['CXI', 'XL', 'LV', 'II']
	for val in range(len(testinp)):
		assert convertnum(testinp[val]) == testout[val]