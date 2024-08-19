import  glob

myfiles = glob.glob("todo/*.txt")

# print(myfiles)
for myfile in myfiles:
    with open(myfile, "r") as file:
        print(file.read().upper())