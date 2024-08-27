def sum_odd_numbers(arr):
    # Find the sum of odd numbers in the array
    total = sum(x for x in arr if x % 2 != 0)
    # Return the sum if it is greater than 25, otherwise return a message
    return total if total > 25 else 'Sum less than 25'

# Example usage:
arr = [1, 4, 6, 7, 10, 12, 11, 5]  # Replace with actual numbers from your array
print(sum_odd_numbers(arr))
