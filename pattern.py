# Solving pattern program in Python

# A square Pattern

n = 5
print("\nA square Pattern")
print()
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print()
    
# Increasing Triangle Pattern
n = 5
print("\nIncreasing Triangle Pattern")
print()
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

# Decreasing Triangle Pattern
n = 5
print("\nDecreasing Triangle Pattern")
print()
for i in range(n):
    for j in range(i,n):
        print("*", end=" ") 
    print()
    
# Right sided triangle

n = 5
print("\nRight Sided Triangle")
print()
for i in range(n):
    
    for j in range(i,n):
        print(' ', end=' ')
        
    for j in range(i+1):
        print('*', end=" ")
        
    print()
    
# Inverted right sided triangle

n = 5
print('\nInverted right sided triangle')
print()
for i in range(n):
    
    for j in range(i+1):
        print(' ', end=' ')
    
    for j in range(i,n):
        print('*', end=' ')
    
    print()
    
# Hill Pattern

n = 5
print("\nHill Pattern")
print()
for i in range(n):
    
    for j in range(i,n):
        print(' ', end=' ')
        
    for j in range(i):
        print('*', end=' ')
        
    for j in range(i+1):
        print('*', end=' ')
    
    print()
    
# Reverse Hil Pattern
n = 5
print("\nReverse Hill Pattern")
print()
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    
    for j in range(i,n-1):
        print('*', end=' ')
        
    for j in range(i,n):
        print('*', end=' ')
    print()

# Diamond pattern

n = 5
print("\nDiamond pattern")
print()
for i in range(n-1):
    
    for j in range(i,n):
        print(' ', end=' ')
    
    for j in range (i+1):
        print('*', end=' ')
        
    for j in range(i):
        print('*', end=' ')
        
    print()
    
for i in range(n):
    
    for j in range(i+1):
        print(' ', end=' ')
    
    for j in range(i,n):
        print('*', end=' ')
    
    for j in range(i,n-1):
        print('*', end=' ')
        
    print()
    
# Pyramid pattern

n = 5
print('\nPyramid Pattern')
print()
for i in range(n):
    
    for j in range (i,n):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print()

# A double hill pattern

n = 5
print('\nA double hill pattern')
print()

for i in range(n):
    for j in range(i,n):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i,n-1):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ') 
        
    print()

# An inverted double hill pattern

n = 5
print('\nAn inverted double hill pattern')
print()
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*', end=' ')
    for j in range(i):
        print(' ', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()
    

 
