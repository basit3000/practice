if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    one, two, three = student_marks[query_name]
    total = (one+two+three)/3
    print("{:.2f}".format(total))
