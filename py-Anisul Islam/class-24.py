# use of list(part-2)

subjects = ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC']
print(len(subjects))
subjects.append('CSS')
print(subjects)
subjects.insert(2,'Tailwind')
print(subjects)
subjects.reverse()
print(subjects)
subjects.remove('OS')
print(subjects)
subjects.pop()
print(subjects)
subjects.clear()
print(subjects)



sub = ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC', 'Dart', 'Bootstrape']
sub.sort()
print(sub)




# or
num = [2, 5, 7, 8, 1, 6, 3, 10, 4, 9]
num.sort()
print(num)


num.reverse()
print(num)


num2 = num.copy()
print(num2)


# 
numbers1 = [10, 20, 30, 40, 50]
pos = numbers1.index(30)
print(pos)



# 
numbers2 = [10, 20, 30, 40, 50, 30, 30, 30]
rain = numbers2.count(30)
print(rain)