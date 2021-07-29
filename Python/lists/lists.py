if __name__ == '__main__':
    n = int(input())
    list0 = []
    for _ in range(n):
        inp = input()
        choice, *v = inp.split()
        v = map(int,v)
        if (choice=="insert"): 
            list0.insert(*v)
        elif (choice=="remove"): 
            list0.remove(*v)
        elif (choice=="append"): 
            list0.append(*v)
        elif (choice=="sort"): 
            list0.sort()
        elif (choice=="reverse"): 
            list0.reverse()
        elif (choice=="pop"): 
            list0.pop(*v)
        elif (choice=="print"): 
            print(list0)
        else: 
            print("invalid command")
            break
