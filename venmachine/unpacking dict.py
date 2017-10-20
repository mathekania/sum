# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
print(type(Counter([('k') * 2, 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])))

# with dictionary
print (Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
print (Counter(A=3, B=5, C=2))

# Python program to demonstrate that counts in
# Counter can be 0 and negative
from collections import Counter

c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)
# Python program to demonstrate accessing of
# Counter elements
from collections import Counter

# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
col_count = Counter(z)
print(col_count)

col = ['blue','red','yellow','green']

# Here green is not in col_count
# so count of green will be zero
for color in col:
    print (color, col_count[color])