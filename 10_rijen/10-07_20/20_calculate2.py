def calculate(a, b, func):
    return func(a, b)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

result1 = calculate(1, 2, add)
result2 = calculate(1, 2, sub)

print(result1, result2)