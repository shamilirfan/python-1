# use of returning value from function

# def add(a, b):
#     sum = a + b
#     return sum

# result = add(20, 30)
# print('Result = ', result)



# 
def large(a, b):
    if a > b :
        return a
    else:
        return b

result = large(20, 30)
print('Result = ', result)
# //
print(large(100, 30))
# //
maximum = large
print(maximum(100, 30))


