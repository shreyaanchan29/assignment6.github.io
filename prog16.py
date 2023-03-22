#. Take inputs from user to make a list. Again take one input from user and search it in the list anddelete that element, if found. Iterate over list using for loop.
my_list = input("Enter a list of elements separated by space: ").split()
to_delete = input("Enter an element to delete from the list: ")
if to_delete in my_list:
 my_list.remove(to_delete)
 print(f"{to_delete} is deleted from the list.")
else:
 print(f"{to_delete} is not found in the list.")
print("Updated list:")
for element in my_list:
 print(element)