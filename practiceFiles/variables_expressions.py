MYINT = 5
MYFLOAT = 11.1
MYSTR = "this is a string"
MYBOOL = True
MYLIST = [0, 1, "two", 3.2, False]
MYTUPLE = (0, 1, 3)
MYDICT = {"one": 1, "two": 2}

print(MYINT)
print(MYFLOAT)
print(MYSTR)
print(MYBOOL)
print(MYLIST)
print(MYTUPLE)
print(MYDICT)

# re-declaring a variable works
MYINT = "abc"
print(MYINT)

# to access a member of a sequence type, use []
print(MYLIST[2])
print(MYTUPLE[1])

# dictionaries are accessed via keys
print(MYDICT["one"])
print(MYDICT["two"])

# ERROR: variables of different types cannot be combined
# print("string type"+ 124)
# TypeError: can only concatenate str (not "int") to str
print("string type " + str(123))

# global vs local variables in functions
def someFunction():
    MYSTR = "def"
    print(MYSTR)

someFunction()
print(MYSTR)

# global vs local variables in functions
# this time i'm affecting the global variable outside the function
def someFunction():
    global MYSTR
    MYSTR = "def"
    print(MYSTR)

someFunction()
print(MYSTR)
