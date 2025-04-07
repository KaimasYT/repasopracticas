import sys
import os
sys.path.append(os.path.abspath("src"))

from src.calculadora import suma, resta

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3
