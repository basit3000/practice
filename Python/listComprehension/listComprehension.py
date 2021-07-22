if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    list0 = []
    list1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if((i+j+k)!=n):
                    list0.append(i)
                    list0.append(j)
                    list0.append(k)
                    list1.append(list0)
                    list0 = []
                    
    print(list1)
