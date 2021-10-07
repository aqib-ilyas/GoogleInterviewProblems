

# Heights array/list
heights = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]

# Getting index of top most element(maximum number) from heights
max_index = heights.index(max(heights))


def calculate_volume(arr=heights,  stop=max_index):
    volume = 0
    start = 0
    end = len(arr)-1
    max_value_start = arr[0]
    max_value_end = arr[-1]

    # Traversing List from Start and End and exit when start reaches end
    while start != end:
        # Calculate volume while traversing
        if start <= stop:
            if(arr[start] > max_value_start):
                max_value_start = arr[start]
            else:
                volume += max_value_start - arr[start]
            start += 1

        if end >= stop:
            if(arr[end] > max_value_end):
                max_value_end = arr[end]
            else:
                volume += max_value_end - arr[end]
            end -= 1
    return volume


print(calculate_volume())
