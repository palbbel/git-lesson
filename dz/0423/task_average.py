def average(lst):
    summ = 0
    for i in lst:
        summ += i

    print(summ)
    aver = round(summ/len(lst), 3)
    print(aver)
    return  aver


average([0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45])