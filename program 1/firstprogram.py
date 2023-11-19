def count_upper_lower_letters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count
input_str = "Hello World! How Are You?"
upper, lower = count_upper_lower_letters(input_str)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
