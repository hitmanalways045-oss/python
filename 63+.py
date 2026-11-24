def test(a, b):
    if a > b:
        return a
    return b

x = test(5, 8)
y = test(10, 3)

print(x)
print(y)
