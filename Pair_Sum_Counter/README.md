# Counting Pairs with a Given Sum

This Python script counts the number of pairs in a list that sum up to a given target value.

## Problem Description

Given a list of integers and a target sum, the script calculates the number of pairs that add up to the target.

## How It Works

1. A dictionary stores the frequency of each number in the list.
2. For each number, the complement (`target_sum - num`) is calculated.
3. If the complement exists in the dictionary, the frequency of the complement is added to the count of valid pairs.
4. The frequency of the current number is updated in the dictionary.

## Example

For the input `l = [1, 2, 3, 4, 5, 4, 3, 2, 1]` and `target_sum = 6`, the output is `7`.

## How to Run

1. Navigate to the folder:
   ```bash
   cd Pair_Sum_Counter
   ```
2. Run the script:
   ```bash
   python3 count_pairs.py
   ```
