# Course Section: CSC 2720-012


def arr_resize(arr, capacity, isUpsizing):
    if isUpsizing:
        new_arr = [None] * int(capacity * 1.25)
    else:
        new_arr = [None] * int(capacity * 0.75)
    new_arr[: len(arr)] = arr[: len(new_arr)]  # Slices and also Copies elements from right-side onto left-side
    print(new_arr)


arr_resize([1, 2, 3, 4, 5, 6, 7, 8], 8, True)  # Expected output [1,2,3,4,5,6,7,8,None,None]
arr_resize([1, 2, 3, 4], 4, True)  # Expected output [1,2,3,4,None]
arr_resize([1, 2, 3, None, None, None, None, None], 8, False)  # [1,2,3,None,None,None]
arr_resize([1, 2, 3, None, None, None], 6, False)  # [1,2,3,None]
