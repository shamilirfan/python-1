# use of xargs and xxargs

def student(*details):
    print(details)

student(101, 'Shamil Irfan')
student(102, 'Shahin Ahmed')



# 
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)


# use of xxargs
def student(**details):
    print(details)
    print(details['id'])

student(id=101, name='Sadman')

