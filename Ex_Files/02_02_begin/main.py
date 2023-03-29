greet = "Hello World"
extedned_grt = "Hello World, " + "this is a long string"

name = "John"

# print("hello" + name)

intrupution = f"Hello {name} cho"


greet_format = "Hello {} cho"

formatted = greet_format.format(name)

print(greet, "\t", extedned_grt, intrupution, "\n", formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Henry"))
