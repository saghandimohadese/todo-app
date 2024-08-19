feet_inches = input("enter feet and inches: ")


def parse(unit):
    parts = unit.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.254
    return meters


parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet and {parsed["inches"]} is equal to {result}")
