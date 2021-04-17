a = [10, 20, 30, 40, 50]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

d = {}
for key, value in zip(a, b):
    d[key] = value

print(d)
