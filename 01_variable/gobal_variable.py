x = "MoizScritz"


def global_variable():

    print("My name is ", x)


global_variable()

y = "MoizScriptz"


def variable():
    global y
    y = "Global Variable"


variable()
print("This is Global Variable", y)
