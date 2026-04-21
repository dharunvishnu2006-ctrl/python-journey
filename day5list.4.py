marks = [85,92,78,95,88]

def find_topper(marks):
    return max(marks)
def find_average(marks):
    return sum(marks)/ len(marks)
def find_failures(marks):
    failures=[]
    for mark in marks:
        if mark < 80:
            failures.append(mark)
    return failures
print("Topper mark:", find_topper(marks))
print("Average:", find_average(marks))
print("Failures:", find_failures(marks))        