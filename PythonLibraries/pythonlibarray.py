import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)
# performing opartion on my_array
print("Array * 2:", my_array * 2)
print("Mean:", np.mean(my_array))
print("Square Roots:", np.sqrt(my_array))

# Practice task
# Create an array with numbers 10 to 50. Find the maximum and minimum values. Multiply all elements by 3.

my_array2 = np.arange(10, 51)

max_val = np.max(my_array2)
min_val = np.min(my_array2)

multiplied_values = my_array2 * 3

print("My Arrays(10-50): ", my_array2)
print("Min_array:", min_val)
print("Max_array:", max_val)
print("Multiplied arrays by 3:", multiplied_values)


