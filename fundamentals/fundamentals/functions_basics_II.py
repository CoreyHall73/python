# Countdown
def countdown(num):
    newList = []
    for i in range(num, 0 - 1, -1):
        newList.append(i)
    return newList

print(countdown(5))


# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([1,2])


#First Plus Length
def first_plus_length(list):
    return list[0] + list[len(list) - 1]

print(first_plus_length([1,2,3,4,5]))


# Values Greater than Second
def values_greater_than_second(list):
    newList = []
    counter = 0
    for i in range(len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
            counter += 1
    print(counter)
    return newList

print(values_greater_than_second([5,2,3,1,4]))


# This Length That Value
def length_and_value(size, value):
    return_list = []
    for i in range(size):
        return_list.append(value)
    return return_list

print(length_and_value(4,7))
print(length_and_value(6,2))