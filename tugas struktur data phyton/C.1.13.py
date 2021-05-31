def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]
print(myReverse([20, 30, 45, 55, 62, 72, 81]))
