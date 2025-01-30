# Roman Numeral Converter

This Python script converts an integer to its corresponding Roman numeral.

## Problem Description

Roman numerals are represented by seven symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`. The script handles special cases where subtraction is used (e.g., `4` is written as `IV`).

## How It Works

1. A list of tuples maps Roman numeral symbols to their corresponding integer values.
2. The algorithm iterates through the list, subtracting values from the input number and appending symbols to the result string.
3. The process continues until the number is reduced to `0`.

## Example

For the input `num = 58`, the output is `"LVIII"`.

## How to Run

1. Navigate to the folder:
   ```bash
   cd Roman_Numeral_Converter
   ```
2. Run the script:
   ```bash
   python3 number_to_roman.py
   ```
