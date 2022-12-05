# use of list as input from user

# n = input('Enter a text of numbers : ')
# list = n.split()
# sum = 0

# for num in list:
#     sum = sum + int(num)

# print(sum)



# 
numofWords = 0
numofLetters = 0
numofDigits = 0

l = input('Enter a text of numbers : ')

for x in l:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofLetters = numofLetters + 1
    elif x >= '0' and x <= '9':
        numofDigits = numofDigits + 1
    elif x == '' :
        numofWords = numofWords + 1

print('Number of Letters : ',numofLetters)
print('Number of Digits : ',numofDigits)
print('Number of Words : ',numofWords + 1)





