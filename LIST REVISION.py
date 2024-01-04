# Create list
l=list(("apple","mango","cherry","kiwi","banana","orange"))
print(l)

#List Type
list=["apple","mango","cherry","kiwi","banana","orange"]
print(type(list))


# List Slicing
l1=[1,2,3,4,5,6,7,8,9]
print("Index value : ",l1[0])
print("Middle value : ",l1[5])
print("Last value : ",l1[-1])

# List Item chages
list=["apple","mango","cherry","kiwi","banana","orange"]
list[1:3]=["grapes","watermelon"]
print(list)

# Insert into list
l2=[1,2,3,4,5,6,7,8,9]
l2.insert(2,100)
print(l2)

# Extend list
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l1.extend(l2)
print(l1)

# Remove list
l1=[1,2,3,4,5,6,7,8,9]
l1.remove(5)
print(l1)

# Pop method 
l1=[1,2,3,4,5,6,7,8,9]
l1.pop(6)
print(l1)

# Delete Method
l1=[1,2,3,4,5,6,7,8,9]
del l1[4]
print(l1)

# Clear method
l1=[1,2,3,4,5,6,7,8,9]
l1.clear()
print(l1)

