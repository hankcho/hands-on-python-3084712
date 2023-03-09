# # this will cause an error
# x = 10 / 0

# # exceptions provide a way of catching errors and then handling them
# try:
#     x = 10 / 0
# except:
#     print("well that didn't work")

# you can also catch specific exceptions
try:
    answer = input("what should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("you can't divide by zero")
    print(e)
except ValueError as e:
    print("you didn't give me a valid number")
    print(e)
finally:
    print("this code always runs")