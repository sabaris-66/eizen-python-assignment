def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    # Initialize a set to store unique characters in the current window
    char_set = set()
    
    # Initialize pointers for the sliding window
    left = 0
    max_length = 0
    
    # Iterate through the string using the right pointer
    for right in range(len(s)):
        # If the current character is already in the set, move the left pointer
        while s[right] in char_set:
            # Remove the character at the left pointer from the set
            char_set.remove(s[left])
            # Move the left pointer to the right
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length if the current window is larger
        max_length = max(max_length, right - left + 1)
    
    # Return the maximum length found
    return max_length


# Example usage
if __name__ == "__main__":
    s = "abcabcbb"
    print(f"Input: {s}")
    print(f"Output: {length_of_longest_substring(s)}")