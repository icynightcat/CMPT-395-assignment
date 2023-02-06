import unittest
def fizz_buzz(num):
    '''
    Description:takes a number and checks if it is a multiple of 3, 5 or both and returns the appropriate string, otherwise returns a string
    representation of that number
    Parameters: num:Integer
    Returns: String fizzbuzz: if multiple of both 5 and 3
    string Fizz: if multiple of fizz
    string buzz: if multiple of 5
    string number: if multiple fo niether 3,5,or both
    '''

    if ((num % 3) == 0 and (num % 5) == 0):
        return ("FizzBuzz")
    elif ((num % 3) == 0):
        return ("Fizz")
    elif ((num % 5) == 0):
        return ("Buzz")
    else:
        return str(num)

class TestPassword(unittest.TestCase):
    
    def test1(var):
        '''The plan is to check the first 15 numbers and then only the multiples'''
        var.assertTrue(fizz_buzz(1) == "1") 
        var.assertTrue(fizz_buzz(2) == "2")
        var.assertTrue(fizz_buzz(3) == "Fizz")
        var.assertTrue(fizz_buzz(4) == "4")
        var.assertTrue(fizz_buzz(5) == "Buzz")
        var.assertTrue(fizz_buzz(6) == "Fizz")
        var.assertTrue(fizz_buzz(7) == "7")
        var.assertTrue(fizz_buzz(8) == "8")
        var.assertTrue(fizz_buzz(9) == "Fizz")
        var.assertTrue(fizz_buzz(10) == "Buzz")
        var.assertTrue(fizz_buzz(11) == "11")
        var.assertTrue(fizz_buzz(12) == "Fizz")
        var.assertTrue(fizz_buzz(13) == "13")
        var.assertTrue(fizz_buzz(14) == "14")
        var.assertTrue(fizz_buzz(15) == "FizzBuzz")
        var.assertTrue(fizz_buzz(18) == "Fizz")
        var.assertTrue(fizz_buzz(20) == "Buzz")
        var.assertTrue(fizz_buzz(21) == "Fizz")
        var.assertTrue(fizz_buzz(23) == "23")
        var.assertTrue(fizz_buzz(24) == "Fizz")
        var.assertTrue(fizz_buzz(25) == "Buzz")
        var.assertTrue(fizz_buzz(27) == "Fizz")
        var.assertTrue(fizz_buzz(30) == "FizzBuzz")
        
        
if __name__ == '__main__':
    unittest.main()
