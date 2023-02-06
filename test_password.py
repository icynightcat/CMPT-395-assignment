import unittest
from string import punctuation

def password_checker(password):
    '''
    Description: takes a string and checks if it is 8 characters long, if it contains 2 numbers in it, if it has atleast one capital letter 
    and if it has a special character
    Parameters: string: password
    Returns: string: ok if the password is okay, otherwise lets the user know what the password is missing
    '''
    countNumbers = 0
    isUpper = False
    isSpecial = False
    final = ""
    
    for i in password:
        if (i.isdigit()): countNumbers= countNumbers + 1
        if (i.isupper()): isUpper = True
        if (i in punctuation): isSpecial = True

    if (len(password) != 8):
        final = final + "Password must be at least 8 characters"
        if (countNumbers < 2):
            final = final + "\nThe password must contain at least 2 numbers"
            if (isUpper == False): 
                final = final + "\nPassword must contain atleast one capital letter"
                if (isSpecial == False): 
                    final = final + "\nPassword must contain at least one special character"
                    return final
                else:
                    return final
            else:
                if (isSpecial == False): 
                    final = final + "\nPassword must contain at least one special character" 
                    return final
                else:
                    return final               
        else:
            if (isUpper == False): 
                final = final + "\nPassword must contain atleast one capital letter"
                if (isSpecial == False): 
                    final = final + "\nPassword must contain at least one special character"
                    return final 
                else:
                    return final           
            else:
                if (isSpecial == False): 
                    final = final + "\nPassword must contain at least one special character"
                    return final
                else:
                    return final               

    if (countNumbers < 2):
        final = final + "The password must contain at least 2 numbers"
        if (isUpper == False):
            final = final + "\nPassword must contain atleast one capital letter"
            if (isSpecial == False): 
                final = final + "\nPassword must contain at least one special character"
                return final
            else:
                return final
        else:
            if (isSpecial == False): 
                final = final + "\nPassword must contain at least one special character"
                return final
            else:
                return final
    
    if (isUpper == False):
        final = final + "Password must contain atleast one capital letter"
        if (isSpecial == False): 
            final = final + "\nPassword must contain at least one special character"
            return final
        else:
            return final
    
    if (isSpecial == False): 
        final = final + "Password must contain at least one special character"
        return final
    else: 
        final = final + "ok"
        return final
    

class TestPassword(unittest.TestCase):
    
    def test1(var):
        '''This is checking all the 8 letter passwords and its various combinations'''
        var.assertTrue(password_checker("AB@12fgh") == "ok")  

        '''checks one missing element in password'''
        var.assertTrue(password_checker("AB@1hfgh") == "The password must contain at least 2 numbers")
        var.assertTrue(password_checker("ab@12fgh") == "Password must contain atleast one capital letter")
        var.assertTrue(password_checker("ABh12fgh") == "Password must contain at least one special character")

        '''checks combination of missing elements in password'''
        var.assertTrue(password_checker("ahj12fgh") == "Password must contain atleast one capital letter\nPassword must contain at least one special character")
        var.assertTrue(password_checker("an@fghkl") == "The password must contain at least 2 numbers\nPassword must contain atleast one capital letter")
        var.assertTrue(password_checker("ABko2fgh") == "The password must contain at least 2 numbers\nPassword must contain at least one special character")
        
        '''This is checking all the non 8 letter passwords'''

        '''checks one missing element in password'''
        var.assertTrue(password_checker("abcdefg") == "Password must be at least 8 characters\nThe password must contain at least 2 numbers\nPassword must contain atleast one capital letter\nPassword must contain at least one special character")
        var.assertTrue(password_checker("ab@dEfg") == "Password must be at least 8 characters\nThe password must contain at least 2 numbers")
        var.assertTrue(password_checker("12c@efg") == "Password must be at least 8 characters\nPassword must contain atleast one capital letter")
        
        '''checks combination of missing elements in password'''
        var.assertTrue(password_checker("aAc12fg") == "Password must be at least 8 characters\nPassword must contain at least one special character")
        var.assertTrue(password_checker("ab12efg") == "Password must be at least 8 characters\nPassword must contain atleast one capital letter\nPassword must contain at least one special character")
        var.assertTrue(password_checker("abc@") =="Password must be at least 8 characters\nThe password must contain at least 2 numbers\nPassword must contain atleast one capital letter")
        var.assertTrue(password_checker("abcA") =="Password must be at least 8 characters\nThe password must contain at least 2 numbers\nPassword must contain at least one special character")
        
if __name__ == '__main__':
    unittest.main()
    #print(password_checker("12c@efg"))