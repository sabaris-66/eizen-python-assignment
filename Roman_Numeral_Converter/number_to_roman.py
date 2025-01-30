def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.
    
    :param num: Integer to convert (1 <= num <= 3999)
    :return: Roman numeral as a string
    """
    # Define tuples for Roman numerals and their corresponding integer values
    # The tuples are ordered from largest to smallest to simplify the conversion process
    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    
    # Initialize an empty string to store the Roman numeral
    roman_numeral = ""
    
    # Iterate through the Roman numeral tuples
    for symbol, value in roman_numerals:
        # While the current value can be subtracted from the number
        while num >= value:
            # Append the Roman numeral symbol to the result string
            roman_numeral += symbol
            # Subtract the value from the number
            num -= value
    
    # Return the final Roman numeral string
    return roman_numeral


# Example usage
if __name__ == "__main__":
    num = 4
    print(f"Input: {num}")
    print(f"Output: {int_to_roman(num)}")