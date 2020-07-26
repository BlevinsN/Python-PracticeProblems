def fun(s):
    # return True if s is a valid email, else return False
    atIndex = s.find('@')
    extentionIndex = s.find('.')
    if atIndex > extentionIndex or atIndex < 1 or extentionIndex == -1:
        return False
    for x in range(0, atIndex):
        if not((s[x] >= 'a' and s[x] <= 'z') or (s[x] >= 'A' and s[x] <= 'Z') or (s[x] >= '0' and s[x] <= '9') or s[x] == '-' or s[x] == '_'):
            return False
    for x in range(atIndex+1, extentionIndex):
        if not(s[x].isalnum()):
            return False
    if not(extentionIndex+4 > len(s)-1):
        return False
    return True
