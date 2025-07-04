furits = ("Orange", "Apple", "Banana", "Grapes")

# Tuples are immutable, so we cannot change them directly.

# However, we can convert the tuple to a list, modify it, and then convert it back to a tuple.

furits_list = list(furits)  # Convert tuple to list

print(furits_list)
print(type(furits_list))

# Now we can modify the list
print("Modifying the list")
furits_list.append("Mango")  # Add a new element
furits_list[1] = "Kiwi"  # Change an existing element
print(furits_list)

print("Updated tuples")
updated_furits = tuple(furits_list)  # Convert list back to tuple

print(updated_furits)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
