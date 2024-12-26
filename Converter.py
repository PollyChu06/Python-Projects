def roman_to_int(numeral):
    # Define a dictionary to store the integer values of Roman numerals
    roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    # Initialize the final integer answer to 0
    final_answer = 0
    # Initialize the previous value to 0 for comparison
    prev_value = 0

    # Iterate through the Roman numeral string in reverse order
    for char in reversed(numeral):
        # Get the integer value of the current Roman numeral character
        value = roman_values.get(char, 0)
        # Check if the current value is less than the previous value (subtractive case)
        if value < prev_value:
            # Subtract the current value from the final answer
            final_answer -= value
        else:
            # Add the current value to the final answer
            final_answer += value
        # Update the previous value for the next iteration
        prev_value = value

    # Return the final integer representation of the Roman numeral
    return final_answer

# Get Roman numeral input from the user
numeral_input = input("Enter the roman numerals you want to convert: ")
# Call the roman_to_int function to convert the Roman numeral to an integer
result = roman_to_int(numeral_input)
# Print the result to the console
print(f"The roman numerals you entered translates to: {result}!")

