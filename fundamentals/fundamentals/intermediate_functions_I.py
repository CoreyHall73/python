# 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Update X
x[1][0] = 15
print(x)
# Change lastname
students[0]["last_name"] = 'Bryant'
print(students[0])
# Change Messi
sports_directory["soccer"][0] = 'Andres'
print(sports_directory["soccer"])
# Change z
z[0]["y"] = 30
print(z[0])




# 2 Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for i in range(0, len(some_list), 1):
        x = some_list[i]
        print(x)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 




# 3 Get Values
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list), 1):
        print(some_list[i][key_name])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('first_name', students)



# 4 Iterate Through
def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i)
        for j in range(0, len(some_dict[i]), 1):
            print(some_dict[i][j])


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
