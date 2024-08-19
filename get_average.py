def get_average(filename):
    with open(filename, "r") as file:
        data = file.readlines()[1:]

    values = [float(i) for i in data]
    data = sum(values)/len(values)
    return data

average1 = ("file.txt")
average2 = get_average("numbers.txt")
print(average1, average2)
