def hornersRule(X,A):
    P = 0

    for digit in A:
        if (digit.isdigit()):
            a = int(digit)
        else: 
            a  = ord(digit) - ord("a") + 10
        P = P*X + a

    return P


def hornersRuleMod(x,A,m):
    P = 0

    for digit in A:
        if (digit.isdigit()):
            a = int(digit)
        else: 
            a  = ord(digit) - ord("a") + 10
        P = (P*x + a) % m + 1

    return P

print(hornersRule(2, "123456789"))
print(hornersRuleMod(2, "123456789"))