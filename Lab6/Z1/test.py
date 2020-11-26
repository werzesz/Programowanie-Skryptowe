import main
import io
import unittest
from unittest.mock import patch
from operacje import Operacje
 
 
class testDecorators(unittest.TestCase):
    @patch('builtins.print')
    def test_suma(self, mock_print):
        op = Operacje()
        op.suma(1, 2, 3)
        mock_print.assert_called_with("1+2+3=6")
        op.suma(1, 2)
        mock_print.assert_called_with('1+2+4=7')
        op.suma(1)
        mock_print.assert_called_with('1+4+5=10')
        op.suma()
        mock_print.assert_called_with(
            'TypeError: suma() takes exactly 3 arguments (2 given)')
''' 
    @patch('builtins.print')
    def test_roznica(self, mock_print):
        op = Operacje()
        op.roznica(2, 1)
        mock_print.assert_called_with("2-1=1")
        op.roznica(2)
        mock_print.assert_called_with('2-4=-2')
        wynik = op.roznica()
        print(wynik)
        mock_print.assert_called_with(6)
''' 
 
if __name__ == '__main__':
    unittest.main()
