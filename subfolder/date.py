date=input("enter today`s date:")
mood=input("how do you rate your mood today from 1 to 10")
thoughts=input("let your thoughts flow:\n")


with open (f"journal/{date}.txt","w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)