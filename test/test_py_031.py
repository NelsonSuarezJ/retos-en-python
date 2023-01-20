import unittest
from py_031 import par_impar


class MyTest(unittest.TestCase):
    '''test'''

    def test_31(self):
        '''Testea que sea par o impar'''
        par = 'Es un numero par'
        impar = 'Es un numero impar'
        self.assertEqual(par_impar(2), par)
        self.assertEqual(par_impar(7), impar)


if __name__ == '__main__':
    unittest.main()
