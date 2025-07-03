# Boolean Values

print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False


print(bool("Hello"))
print(bool(15))
print(bool())


def myFunction():
    return False


if myFunction():
    print("YES!")
else:
    print("NO!")

# KEY ISINSTANCE

x = 351
print(isinstance(x, int))
