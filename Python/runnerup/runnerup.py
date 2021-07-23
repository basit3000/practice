if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr, reverse=True)
    condition = True
    second = 0
    if(n>=2 and n<=10):
        for i in range(n):
            if(arr[i]<-100 or arr[i]>100):
                condition = False
        if(condition==True):
            for j in range(n):
                if(max(arr)!=arr[j]):
                    second = arr[j]
                    print(second)
                    break
