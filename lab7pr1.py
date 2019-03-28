def uppercount(s):
    if s == "":
        return 0
    else:
        if ord(s[0]) <= 90 and ord(s[0]) >= 65:
            return 1 + uppercount(s[1:])
        else:
            return uppercount(s[1:])

print(uppercount("HappyHH"))
