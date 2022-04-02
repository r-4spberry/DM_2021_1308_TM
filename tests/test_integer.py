import sys
import os
import random
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from integer import *

class TestInt(unittest.TestCase):
    pass
    #Делаем на подобии того, как в test_natnum.py
    #На каждой функции стараемся все возможные крайние случаи
    #На правильность типа можно пока забить

def main():
    unittest.main()
    
if __name__ == "__main__":
    main()
    
