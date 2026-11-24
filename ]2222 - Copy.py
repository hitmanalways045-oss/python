import copy

a = {"x": [1, 2, 3], "y": 10}
b = copy.deepcopy(a)

b["x"][0] = 99
print(a)
print(b)
