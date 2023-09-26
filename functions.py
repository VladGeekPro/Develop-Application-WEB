# Create a function without arguments, a second one with 2 arguments,a third one with default argument, and a fourth one that returs a value
def fun1():
    print("Life is good")

def fun2(var1, *var2):
    print("\nI like {0},but most of the time I eat {1}".format(var1, var2))

def fun3(var1 = "sunshine", var2 = {1, 1, 2, 3, 4, 4 }):
    print(var1) if (len(var2) < 4) else print("Cloud")

def fun4(var1):
    return {
        "one" : "Summer",
        "two" : "Forest",
        "three" : "Fire"
    }.get(var1, "Winter")

# Create and use a lambda function
List1 = []
funlambda = lambda str : List1.append(str[-1])