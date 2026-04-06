s=input()
def romantoInt(s):
    value={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}

    result =0

    for i in range(len(s)):
        if i < len(s) -1 and  value[s[i]]< value[s[i+1]]:
            result-=value[s[i]]
        else:
            result+=value[s[i]]
    return result

print(romantoInt(s))