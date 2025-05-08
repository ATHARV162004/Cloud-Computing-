def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Greedily place the minimum at the beginning of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1}: {arr}")
    return arr

# Get user input
user_input = input("Enter numbers to sort (space-separated): ")
arr = list(map(int, user_input.split()))

# Run selection sort
print("\nSelection Sort Process:")
sorted_arr = selection_sort(arr)
print("\nSorted Array:", sorted_arr)

