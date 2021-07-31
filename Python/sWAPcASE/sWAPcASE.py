def swap_case(s):
    t = ""
    for i in range(len(s)):
        if(s[i].isupper() == True):
            t += s[i].lower()
        elif(s[i].isupper() == False):
            t += s[i].upper()
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
