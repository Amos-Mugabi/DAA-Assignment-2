def counting_sort(arr):
    # Find the maximum element in the input array
    max_element = max(arr)
    
    # Create a counting array to store the count of each element
    count = [0] * (max_element + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    
    # Calculate the starting index for each element in the sorted output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create the output array and place the elements in their correct positions
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print("Sorted Array:", sorted_array)



