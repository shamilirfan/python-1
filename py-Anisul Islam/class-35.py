# use of stack and queue

# lifo = first in last out
# books = []
# books.append('Learn C')
# books.append('Learn C++')
# books.append('Learn Javascript')
# print(books)
# # //
# books = []
# books.append('Learn C')
# books.append('Learn C++')
# books.append('Learn Javascript')
# print(books)
# books.pop()
# print(books)
# books.pop()
# print(books)
# # //
# books = []
# books.append('Learn C')
# books.append('Learn C++')
# books.append('Learn Javascript')
# books.pop()
# print(books)
# print('Now the top book is : ', books[-1])
# # print('Now the top book is : ', books[-2])








# ********** use of queue **********
# fifo = first in first out

from collections import deque

bank = deque(['Shahin', 'Shakil', 'Sadman', 'Sabbir'])
print(bank)
bank.popleft()
print(bank)



