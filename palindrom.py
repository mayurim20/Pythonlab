def palindrome(s):
    if(s[::-1]==s[0::]):
        print(s,"is palindrome")
    else:
        print("not palindrome")
s=input("enter a string:")
palindrome(s)
