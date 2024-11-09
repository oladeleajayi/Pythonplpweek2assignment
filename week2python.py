# # Question 1.creating an empty list
my_list=[]

# # # Question 2.Append the following elements to my_list: 10, 20, 30, 40.
my_list=[10,20,30,40]
print(my_list)

# # # Question 3.Insert the value 15 at the second position in the list
my_list.insert(1,15)
print(my_list)

# # # Question 4.Extend my_list with another list: [50, 60, 70]
my_list=[10,15,20,30,40]
addittional_list=[50,60,70]
my_list.extend(addittional_list)
print(my_list)

# # Question 5.Remove the last element from my_list.
# # Method 1:Using pop()
my_list=[10,15,20,30,40,50,60,70]
removed_element=my_list.pop()
print(my_list) #[10,15,20,30,40,50,60,70]
print(removed_element) #70

# # Method 2:Using remove() with index
my_list=[10,15,20,30,40,50,60,70]
removed_element=my_list.pop(-1) # or my_list.remove(my_list[-1])
print(my_list) #[10,15,20,30,40,50,60,70]

# # Method 3:Using list slicing
my_list=[10,15,20,30,40,50,60,70]
my_list=my_list[:-1] # or my_list.remove(my_list[-1])
print(my_list) #[10,15,20,30,40,50,60,70]

# # Question 6.Sort my_list in ascending order.
# Method 1.Using sort()
my_list=[10,15,20,30,40,50,60]
my_list.sort()
print(my_list)

# # Method 2.Using sorted()
my_list=[10,15,20,30,40,50,60]
my_list=sorted(my_list)
print(my_list)

# # Question 7.Find and print the index of the value 30 in my_list.
# # Method 1.Using index()
my_list=[10,15,20,30,40,50,60]
index=my_list.index(30)
print(index) # 3

# Method 2.Using enumerate()
my_list=[10,15,20,30,40,50,60]
for i,value in enumerate(my_list):
    if value==30:
        index=i
        break
print(index) # 3