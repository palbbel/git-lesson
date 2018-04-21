def bubble_sort(lst):
    for i in range(len(lst)-1):
        k = len(lst) - 1
        while k != i:
            print(k)
            print(lst[k])
            print(lst[k - 1])
            if lst[k] < lst[k - 1]:
                lst[k - 1], lst[k] = lst[k], lst[k - 1]
                print(lst)
            k -= 1

    print(lst)

bubble_sort([6,5,2,9,4,33,1,77,32,45,3])
