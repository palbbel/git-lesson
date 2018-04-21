def is_palindrome(s):
    revers_s = ''
    s = str(s)

    for i in s[::-1]:
        revers_s += i

    s = "".join(s.lower().split())
    revers_s = "".join(revers_s.lower().split())
    if s == revers_s:
        print('True')
        return True
    elif s != revers_s:
        print('False')
        return False


is_palindrome('Селg в озере березов g gлес')

'''
"".join(s.lower().split())
"".join(revers_s.lower().split())

s[::-1].strip()
'''