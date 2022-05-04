# Creating a list
new_list = [7,8,9,2,3,1,4,10,5,6]
print(new_list)

# Sort the list (asc.)
sorted_list = new_list
sorted_list.sort()
print(sorted_list)

# Sort the list (desc.)
sorted_list_desc = new_list
sorted_list_desc.sort(reverse=True)
print(sorted_list_desc)

# Printing the x*3 numbers
for x in new_list:
    if x % 3 == 0:
        print(x)

# Printing the odd/even nr.
for y in new_list:
    if y % 2 > 0:
        print('This is an odd number',y)
    else: print('This is an even number', y)