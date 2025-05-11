# Link:
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda interval: interval[0])
    start = 0
    finish = 1
    result = 0
    previous = 0

    for interval in range(len(intervals)):
        if interval == 0:
            result += intervals[interval][finish] - intervals[interval][start]
            continue

        a = intervals[previous]
        b = intervals[interval]

        if b[finish] <= a[finish]:
            continue
        elif b[start] < a[finish] and b[finish] > a[finish]:
            result += b[finish] - a[finish]
        elif b[start] >= a[finish]:
            result += b[finish] - b[start]
        previous = interval

    return result
