def find_number_of_superior_elements(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize the count of superior elements
    count = 1  # The rightmost element is always a superior element
    max_from_right = arr[-1]  # Start with the rightmost element

    # Traverse the array from right to left
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            count += 1
            max_from_right = arr[i]

    return count

# Example usage:
arr = [10, 4, 6, 3, 5]
print(find_number_of_superior_elements(arr))  # Output: 3
