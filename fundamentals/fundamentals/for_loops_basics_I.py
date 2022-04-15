# Print 0 to 150
for i in range(151):
    print(i)


# Multiples of 5
for i in range(5, 1001, 5):
    print(i)


# Counting
for i in range(1, 101):
    if (i % 5 == 0) and (i % 10 == 0):
        i = "Coding Dojo"
    elif i % 5 == 0:
        i = "Coding"
    print(i)


# Huge
sum = 0
for i in range(1500001):
    if i % 2 == 1:
        sum += i
print(sum)


# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)


# Flexible Counter
lowNum = 2
highNum = 9
mult = 3 
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)
