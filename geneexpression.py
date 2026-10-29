def filter_expression(values, threshold=5.0):
    return [ x for x in values if x > threshold]
expression = [2.5, 7.1, 0.8, 5.4, 9.2, 3.0]
n = float(input())
print(filter_expression(expression, threshold=n))
