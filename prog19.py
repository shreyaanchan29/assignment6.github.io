# From a list containing ints, strings and floats, make three lists to store them separately
original_list = [1, "hello", 3.14, 42, "world", 2.718]
int_list = []
str_list = []
float_list = []
for element in original_list:
 if type(element) == int:
  int_list.append(element)
 elif type(element) == str:
  str_list.append(element)
 elif type(element) == float:
  float_list.append(element)
print("Integers:", int_list)
print("Strings:", str_list)
print("Floats:", float_list)