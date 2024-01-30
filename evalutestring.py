alphabet = "(abcdefghijklmnopqrstuvwxyz)"

# obtain user input for the range of alphabet
user_range = input("put a range of alphabet (e.g., a-z): ")

# Extract start and end letters from the user input
start_letter, end_letter = user_range.split("-")

# Find the indices of start and end letters in the alphabet
start_index = alphabet.index
end_index = alphabet.index(end_letter)

# Create a substring using the provided indices
result_string = alphabet[start_index:end_index]

# Print the result
print(result_string)


