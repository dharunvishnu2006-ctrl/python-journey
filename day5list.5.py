marks = [85, 92, 78, 95, 88]
failures = []
for mark in marks:
    if mark < 80:
        failures.append(mark)
print("Normal:", failures)
failures = [mark for mark in marks if mark < 80]
print("Shortcut:", failures)
doubled = [mark * 2 for mark in marks]
print("Doubled:", doubled)