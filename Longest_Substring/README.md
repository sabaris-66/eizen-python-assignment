# Longest Substring Without Repeating Characters

This Python script finds the length of the longest substring in a string that does not contain any repeating characters.

## Problem Description

Given a string, the script calculates the length of the longest substring without repeating characters.

## How It Works

1. A sliding window approach is used with two pointers (`left` and `right`) to track the current substring.
2. A set stores unique characters in the current window.
3. The algorithm expands the window by moving the `right` pointer and contracts it by moving the `left` pointer when a repeating character is encountered.
4. The length of the longest substring is updated during the process.

## Example

For the input `s = "abcabcbb"`, the output is `3`.

## How to Run

1. Navigate to the folder:
   ```bash
   cd Longest_Substring
   ```
2. Run the script:
   ```bash
   python3 longest_substring.py
   ```
