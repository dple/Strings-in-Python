from itertools import combinations

def isAlternativeString(s):
    L = list(set(s))
    if len(L) != 2:
        return False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

# Complete the alternate function below.
def alternate(s):
    L = set(s)    # get unique characters in the string
    n = len(L)
    if n <= 1:
        return 0
    if n == 2:
        if isAlternativeString(s):
            return len(s)
        else:
            return 0

    combs = list(combinations(L, n - 2))  # get the combinations of length n - 2 in set L
    ret = ''
    for comb in combs:  # scan all combinations in combs
        t_ret = s
        # Remove all charaters in comb appearing in string s
        for c in comb:
            t_ret = t_ret.replace(c, '')
        if isAlternativeString(t_ret) and len(t_ret) > len(ret):
            ret = t_ret
    return len(ret)

if __name__ == '__main__':
    s = 'beabeefeab'
    print(alternate(s))