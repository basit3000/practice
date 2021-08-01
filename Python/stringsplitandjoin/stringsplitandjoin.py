def split_and_join(line):
    line = line.split(" ")
    string = line[0]
    for i in range(1,len(line)):
        string = string + "-" + line[i] 
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
