
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):              # _ is usually used when we don't need the loop variable
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
    
    
    

    
    
    
# ------------ EXPLAINATION --------------
# The * means:  Collect all remaining values into line.
#  name, *line = ['Malika', '52', '56', '60']
# becomes:
# name = 'Malika'
# line = ['52', '56', '60']
