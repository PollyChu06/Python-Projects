def roman_to_int(numeral):
    roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    final_answer = 0
    prev_value = 0

    for char in reversed(numeral):
        value = roman_values.get(char, 0)
        if value < prev_value:
            final_answer -= value
        else:
            final_answer += value
        prev_value = value

    return final_answer

numeral_input = input("Enter the roman numerals you want to convert: ")
result = roman_to_int(numeral_input)
print(f"The roman numerals you entered translates to: {result}!")

