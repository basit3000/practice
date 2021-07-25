if __name__ == '__main__':
    n = int(input())
    dictionary = {}
    arr = []
    for i in range(n):
        name = input()
        score = float(input())
        dictionary[name] = score
        arr.append(score)
    arr2 = sorted(arr)
    condition = True
    second = 0
    if(n>=2 and n<=5):
        for j in range(n):
            if(min(arr2)!=arr2[j]):
                second = arr2[j]
                break
    arr3 = []
    for key in dictionary:
        if(dictionary[key] == second):
            arr3.append(key)      
    arr3 = sorted(arr3)
    for i in range(len(arr3)):
        print(arr3[i])
