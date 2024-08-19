FILEPACH = "todos.txt"
# constants


def get_todos(filename=FILEPACH):

    """
    get_todos returns a list of all todo items from a file and the file is received from argument
    :return: list of todo item
    """
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos


def set_todos(todos, filename=FILEPACH):
    """
    :param todos:set_todos get new todos list and then save in target file
    :param filename:list ot todos
    :return: target file to write todos list
    """

    with open(filename, "w") as file:
        file.writelines(todos)
