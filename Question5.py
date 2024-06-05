#Question 5
def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
n = int(input("Enter number: "))
if is_palindrome(n):
  print("The number is a palindrome.")
else:
  print("The number is not a palindrome.")
