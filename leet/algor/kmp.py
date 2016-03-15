#reference https://github.com/mission-peace/interview/blob/master/python/string/knuthmorrispratt.py

def gen_next(p):
    n = len(p)
    next = [0 for i in range(n)]
    pattern_index = 0
    str_index = 1
    while str_index < n:
        if p[str_index] == p[pattern_index]:
            next[str_index] = pattern_index + 1
            str_index += 1
            pattern_index += 1
        else:
            if pattern_index == 0:
                next[str_index] = 0
                str_index += 1
            else:
                pattern_index = next[pattern_index - 1]

    return next

def kmp(s,p):
    next = gen_next(p)
    l1 = len(s)
    l2 = len(p)
    i = j = 0
    while i < l1 and j < l2:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = next[j-1]

    if j == l2:
        return True
    else:
        return False

print gen_next("abcabc")
print gen_next("aaaaaa")
print kmp("abcabcd","abcabc")
