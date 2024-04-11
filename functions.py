import time

def get_todos(filepath="todo.txt"):
    """
        Read a text a file and return a list of to_do items
    """
    with open(filepath, 'r') as file:
            todos = file.readlines()
    return todos

def write_todos(to_do_list_arg, filepath="todo.txt"):
    """
        Write a to_do items list in the text file
    """
    with open(filepath, 'w') as file:
            file = file.writelines(to_do_list_arg)

def current_time():
    """
        This function tells the user the current date and time
    """
    now = time.strftime('%b %d, %Y %H:%M:%S')
    return f'It is {now}'

if "__name__" == "__main__":
    print(current_time())
