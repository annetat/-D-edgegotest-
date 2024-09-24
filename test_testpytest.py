from ops import *

def test_number():
    number = 2 
    assert number == 2 

def test_multply():
    mult = 3 * 3 
    assert mult == 9

def test_fail():
    mult = 3 * 3 
    assert mult == 2