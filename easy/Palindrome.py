'''
    76ms, faster than 20.43% of python sols
    14.2MB, less than 51.35% of python sols
'''

def isPalindrome(x) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        for digit in range(0, len(str(x))):
            rev = rev * 10 + (x % 10)
            x = int(x/10)
        return rev == temp

a = 121
b = 223

print("121 is a palindrome: " + str(isPalindrome(a)))
print("223 is a palindrome: " + str(isPalindrome(b)))
