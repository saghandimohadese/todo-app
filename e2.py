import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

    city = input("enter city name:")

    for row in data[1:]:
        if row[0] == city:
            print(row[1])
    print(data)

    # shutil.make_archive("output", "zip", "todo")
