#You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
original_list = [1, 2, 3, 4, 5]
squared_list = []
for element in original_list:
 squared_element = element ** 2
 squared_list.append(squared_element)
print("Original List:", original_list)
print("Squared List:", squared_list)