import unittest
from task import conv_num, conv_endian, my_datetime
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        """Check to see if a string is correctly converted to an integer."""
        expected = 12345
        self.assertEqual(conv_num('12345'), expected)

    def test2(self):
        """Check if a string is converted to a negative fractional number."""
        expected = -123.45
        self.assertEqual(conv_num('-123.45'), expected)

    def test3(self):
        """Check to see if a string starting with a decimal is converted."""
        expected = 0.45
        self.assertEqual(conv_num('.45'), expected)

    def test4(self):
        """Check to see if a string ending with a decimal returns a float."""
        expected = 123.0
        self.assertEqual(conv_num('123.'), expected)

    def test5(self):
        """Check to see if a hexadecimal string returns integer value"""
        expected = 2772
        self.assertEqual(conv_num('0xAD4'), expected)

    def test6(self):
        """Check to see if an invalid hexadecimal string returns None"""
        expected = None
        self.assertEqual(conv_num('0xAZ4'), expected)

    def test7(self):
        """Check to see if an invalid string returns None"""
        expected = None
        self.assertEqual(conv_num('12345A'), expected)

    def test8(self):
        """Check to see if an invalid string with two decimals returns None"""
        expected = None
        self.assertEqual(conv_num('12.3.45'), expected)

    def test9(self):
        """Check to see if an invalid hexadecimal string returns None"""
        expected = None
        self.assertEqual(conv_num('0xAZ4x'), expected)

    def test10(self):
        """Check to see if a valid negative hexadecimal string returns integer."""
        expected = -2772
        self.assertEqual(conv_num('-0xAD4'), expected)

    def test11(self):
        """pass in big as an argument for endian"""
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(954786, 'big'), expected)

    def test12(self):
        """pass no argument for endian"""
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(954786), expected)

    def test13(self):
        """pass in a negative number as an argument for num"""
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(-954786), expected)

    def test14(self):
        """pass in little as an argument for endian"""
        expected = 'A2 91 0E'
        self.assertEqual(conv_endian(954786, 'little'), expected)

    def test15(self):
        """pass in a negative number as an argument for num and
         little as an argument for endian"""
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(-954786, 'little'), expected)

    def test16(self):
        """pass in a negative number as an argument for num and
         little as an argument for endian with the name of the
         parameters indicated"""
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(num=-954786, endian='little'), expected)

    def test17(self):
        """pass in a negative number as an argument for num and
         an invalid argument for endian with the name of the
         parameters indicated"""
        expected = None
        self.assertEqual(conv_endian(num=-954786, endian='small'), expected)

    def test18(self):
        """pass in zero as an argument for num"""
        expected = "00"
        self.assertEqual(conv_endian(0), expected)

    def test19(self):
        """Check if 0 gets the start of the epoch"""
        expected = "01-01-1970"
        self.assertEqual(my_datetime(0), expected)

    def test20(self):
        """Check 201653971200 for 2-29-8360, far off date"""
        expected = "02-29-8360"
        self.assertEqual(my_datetime(201653971200), expected)

    def test21(self):
        """Check for 3498972111"""
        t = date.fromtimestamp(3498972111)
        expected = t.strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(3498972111), expected)

    def test22(self):
        """Check for 3236236871"""
        t = date.fromtimestamp(3236236871)
        expected = t.strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(3236236871), expected)


if __name__ == '__main__':
    unittest.main()
