# This sequence is a look-and-say sequence.
# https://www.geeksforgeeks.org/look-and-say-sequence/


def foo(num):
    if num == 1:
        return 11
    s = str(num)
    res = ""
    curSiz = 1
    for i in range(len(s)):
        if i == 0:
            i += 1
            continue
        if s[i] == s[i - 1]:
            curSiz += 1
        else:
            res += str(curSiz)
            curSiz = 1
            res += s[i - 1]
        if i == len(s) - 1:
            res += str(curSiz)
            res += s[i]
            continue
    return int(res)


cur = 1
for i in range(30):
    cur = foo(cur)

print(len(str(cur)))
