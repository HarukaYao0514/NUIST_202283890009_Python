#Author: Yao Yao

def studList():
    studentNames = ['Lisa', 'Liam', 'Leo', 'Larry', 'Linda']
    
    for name in studentNames:
        print(f"{name} Evans")

def addToList():
    studentNames = ['Lisa', 'Liam', 'Leo', 'Larry', 'Linda']
    
    new_name = input("Please enter another first name to add to the list: ")
    
    studentNames.append(new_name)
    
    for name in studentNames:
        print(f"{name} Evans")


print("Original List:")
studList()
    
print("\nAdding a New Name:")
addToList()
