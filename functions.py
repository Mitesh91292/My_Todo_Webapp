FILEPATH = r"C:\Users\mites\Desktop\Udemy Python\Projects\web_app1\TodoWebApp\todos.txt"


def get_todos(filepath=FILEPATH):
    """
    This function gets current list of todos from a text file and stores them in a list variable.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
