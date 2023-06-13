# test_calc.py
from calc import soma, subtracao

def test_soma():
    assert soma(1, 2) == 3

def test_subtracao():
    assert subtracao(3, 2) == 1
