def is_leap(year):
    leap = False
    
    if(year>=1900 and year<=100000):
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):
                    leap = True
                else:
                    leap = False
            else:
                leap = True
    return leap

print(is_leap(1994))
print(is_leap(1992))
