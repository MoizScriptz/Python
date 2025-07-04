set = {"Apple", "Banana", "Cherry", "Orange"}

# Accessing elements in a set is not possible like lists or tuples because sets are unordered collections.
# However, we can check for membership and iterate through the set.
# Checking if an element exists in the set
print("Apple" in set)  # Output: True

set2 = {"Apple", "Banana", "Cherry", "Orange", "Banana"}

# Sets automatically remove duplicates, so the second "Banana" will not be added again.
print(set2)  # Output: {'Apple', 'Banana', 'Cherry', 'Orange'}


set2.add("Mango")  # Adding a new element

print(set2)

set.update(set2)  # Updating set with another set

print(set)  # Output: {'Apple', 'Banana', 'Cherry', 'Orange', 'Mango'}
