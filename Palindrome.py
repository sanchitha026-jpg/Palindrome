import sys
def check(s):
    return s == s[::-1]

s = sys.argv[1]

if check(s):
    print("Palindrome")
else:
    print("Not a palindrome")