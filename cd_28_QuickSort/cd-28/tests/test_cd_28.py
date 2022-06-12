import pytest 
from cd_28.quick_sort import quick_sort_fun



def test_q_s( ):
    actual=quick_sort_fun([8, 4, 23, 42, 16, 15], 0, 5)
    assert actual==[4, 8, 15, 16, 23, 42]


def test_q_s_2( ):
    actual=quick_sort_fun([20, 18, 12, 8, 5, -2], 0, 5)
    assert actual== [-2, 5, 8, 12, 18, 20]

def test_q_s_3( ):
    actual=quick_sort_fun([5, 12, 7, 5, 5, 7], 0, 5)
    assert actual== [5, 5, 5, 7, 7, 12]


 