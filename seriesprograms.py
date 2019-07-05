# PRogram

""" splitting with out using slice"""

s ="Hello World Welcome To Python"
word =''
words =[]
for i in s:
    if i ==' ':
        words.append(word)
        word =''
    else:
        word+=i
else:
    if word:
        words.append(word)
print words

#program
""" 
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
"""
n =5
for i in range(10):
    for j in range(i):
        print i,
    print


# program
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 
"""

for i in range(10):
    for j in range(i):
        print i,
    print

# program3
"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
"""


for i in range(10):
    for j in range(i):
        print '*',
    print

#program 4
""" splitting with out using slice"""
s ="Hello World Welcome To Python"
word =''
words =[]
for i in s:
    if i ==' ':
        words.append(word)
        word =''
    else:
        word+=i
else:
    if word:
        words.append(word)
print words
