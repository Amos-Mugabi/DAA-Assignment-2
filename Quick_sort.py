def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage
if __name__ == "__main__":
    input_list = [12, 4, 5, 6, 7, 3, 1, 15]
    sorted_list = quicksort(input_list)
    print("Sorted list:", sorted_list)
    