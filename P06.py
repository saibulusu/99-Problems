# determine if a list is a palindrome
def isPalindrome(list):
    for i in range(0, len(list) / 2):
        if (list[i] != list[len(list) - i - 1]):
            return False
    return True

# tester code
a = []
assert(isPalindrome(a))

a.append(3)
assert(isPalindrome(a))

a.append(4)
assert(not isPalindrome(a))

a.append(4)
a.append(3)
assert(isPalindrome(a))
