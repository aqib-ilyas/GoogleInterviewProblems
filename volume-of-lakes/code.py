

# Heights array/list
heights = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]


def calculate_volume(arr=heights):
    volume = 0
    left = 0
    right = len(arr)-1
    max_value_left = arr[0]
    max_value_right = arr[-1]

    # Traversing List from Start and End and exit when start reaches end
    while left <= right:
        # Calculate volume while traversing
        if max_value_left <= max_value_right:
            if(arr[left] > max_value_left):
                max_value_left = arr[left]
            else:
                volume += max_value_left - arr[left]
            left += 1
        else:
            if(arr[right] > max_value_right):
                max_value_right = arr[right]
            else:
                volume += max_value_right - arr[right]
            right -= 1
    return volume


print(calculate_volume())
