# modified version of counting sort
def sort_arr_by_digit(arr, round):
    n = len(arr)
    count = [0] * 10  # count based on digits
    output = [0] * n

    for i in range(n):
        digit = (arr[i] // pow(10, round)) % 10
        count[digit] += 1

    # prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // pow(10, round)) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    for i in range(n):
        arr[i] = output[i]
    print("After round #", round + 1, ":", arr)


def radix_sort(arr):
    # determine the number of digits/rounds
    max_num = max(arr)
    rounds = len(str(max_num))

    # Perform sorting rounds
    for round in range(0, rounds):
        sort_arr_by_digit(arr, round)


# Example usage:
arr = [170, 45, 75, 90, 2, 802, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)
