def factorial_product(n):
    if n <=1:
        return "1"
    else:
        return str(n)+"*"+factorial_product(n-1)

def caps(c):
    if ord(c) <= 122 and ord(c) >= 97:
        return chr(ord(c) - 32)
    else:
        return c


def allCaps(s):
    s.split()
    if s == "":
        return ""
    else:
        return caps(s[0]) + allCaps(s[1:])

