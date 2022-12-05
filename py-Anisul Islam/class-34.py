# use of set

num1 = {1, 2, 3, 4, 5}
print(num1)
# //
num2 = {1, 2, 3, 4, 5, 5}
print(num2)




# 
num3 = set([4, 5, 6])
num3.add(7)
print(num3)
# for cheking value
print(4 in num3)
print(4 not in num3)
print(8 in num3)




# 
num4 = {1, 2, 3, 4}
num5 = set([3, 4, 5, 6, 7, 8])
print(num4 | num5)
print(num4 & num5)
print(num4 - num5)