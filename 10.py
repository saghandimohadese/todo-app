# temperatures = [10, 12, 14]
# file = open("file.txt", "w")
# temperatures=[str(i)+"\n" for i in temperatures]
# file.writelines(temperatures)


with open("file.txt","r") as file:
    text=file.read()
    print(text)
    print(len(text))