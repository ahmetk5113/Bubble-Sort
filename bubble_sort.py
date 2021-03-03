def bubble_sort():
    unordered_list = [4,1,7,2,8,3,99]
    upper_bound = len(unordered_list)
    top = upper_bound
    while top != 0:
        for index in range(upper_bound - 1):
            if unordered_list[index] > unordered_list[index + 1]:
                temporary = unordered_list[index]
                unordered_list[index] = unordered_list[index + 1]
                unordered_list[index + 1] = temporary
            print(unordered_list)
        top = top - 1
bubble_sort()