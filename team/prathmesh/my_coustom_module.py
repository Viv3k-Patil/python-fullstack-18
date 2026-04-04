#PI=3.14
#passward=15101453
#username="Darling123"

def find_duplicates_with_set(input_list):
    seen = set()
    duplicates = set()  # Use a set to store unique duplicates to avoid repetition
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

my_list = [1, 2, 3, 4, 5, 2, 6, 3, 1]
print(f"Original list: {my_list}")
duplicate_items = find_duplicates_with_set(my_list)
print(f"Duplicate values: {duplicate_items}")

# Output:
# Original list: [1, 2, 3, 4, 5, 2, 6, 3, 1]
# Duplicate values: [1, 2, 3] (order may vary)
