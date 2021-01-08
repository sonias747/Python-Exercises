'''
Implement the recursive solution presented in lectures for checking whether
given strings input by the user are palindromes.
'''


'''
define isPalindrome function for s
    define toChars function for s
        change string to lowercase
        set letterstring to empty string
        for c in 'a-z'
            increment letterstring by c
        return letterstring

    define isPal function for s
        if length of s in less that or equal to 1
            return true
        else
            return first character equals last character and call isPal function on second first and second last characters of s
    return isPal function of toChars function of s

input user for a string

while string is not an empty character
    if isPalindrome is true
        print string is a palindrome
    else
        print string is not a palindrome
    prompt user for another string

print finished   


'''

def isPalindrome(s):
    """Checks whether the string s is a palindrome

    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""

    def toChars(s):
        """Converts a string to lowercase and removes non-letters

        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letters"""
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring   

                
    def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise.
        Recursive function."""
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))       
        

str = input('Enter a string (empty string to exit): ')

while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:   
        print(str, 'is not a palindrome')

    str = input('Enter a string (empty string to exit): ')

print('Finished!')    
