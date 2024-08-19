def parse(user_input):
    """Extract the values split by a comma in a string
 and return the two values via a dictionary.
 """
    parts = user_input.split(",")

    lower_bound = int(parts[0])
    upper_bound = int(parts[1])

    return {"lower_bound": lower_bound, "upper_bound": upper_bound}
