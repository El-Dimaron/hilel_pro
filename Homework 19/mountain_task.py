# a. 30 minutes: solved about half of the task
# b. 1 hour: full task is solved


def maximum_height(mountain):
    left_pointer = 0
    max_depth = 0

    for right_pointer in range(1, len(mountain)):

        max_height = min(mountain[right_pointer], mountain[left_pointer])
        min_height = min(min(mountain[left_pointer:right_pointer]), mountain[right_pointer])

        if max_height - min_height > max_depth:
            max_depth = max_height - min_height

        if mountain[right_pointer] >= mountain[left_pointer]:
            left_pointer = right_pointer

    return max_depth
