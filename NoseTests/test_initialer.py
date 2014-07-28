import nose
from nose.tools import *
from initialer import *

def test_initials_takes_name_as_an_argument():
    assert_raises(TypeError, initials)

def test_initals_raises_IndexError_if_length_of_name_is_under_3():
    assert_raises(IndexError, initials, "")