def count_pairs_with_sum(arr, target_sum):
    """
    Count the number of pairs in a list that sum up to a given target.

    :param arr: List of integers
    :param target_sum: Target sum to find pairs for
    :return: Number of pairs that sum up to the target
    """
    # Initialize a dictionary to store the frequency of each element in the list
    frequency = {}
    count = 0  # Initialize the count of pairs

    # Iterate through the list
    for num in arr:
        # Calculate the complement (the number needed to form the target sum with the current number)
        complement = target_sum - num

        # If the complement is in the frequency dictionary, add its frequency to the count
        if complement in frequency:
            count += frequency[complement]

        # Update the frequency of the current number in the dictionary
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Return the total count of pairs
    return count


# Example usage
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    target_sum = 6
    print(f"Input list: {l}")
    print(f"Target sum: {target_sum}")
    print(f"Number of pairs: {count_pairs_with_sum(l, target_sum)}")