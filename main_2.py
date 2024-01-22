import functions as f
import time


def current_time():
    """
        This function tells the user the current date and time
    """
    now = time.strftime('%b %d, %Y %H:%M:%S')
    return f'It is {now}' 


current_time()
 
while True:
    user_action = input('Type add, show, complete, edit or exit: ')
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        to_do = user_action[4:]

        to_do_list = f.get_todos()
            
        to_do_list.append(to_do.title() + '\n')

        f.write_todos(to_do_list)         

    elif user_action.startswith('show'):
        to_do_list = f.get_todos()

        for index, item in enumerate(to_do_list):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            position = number - 1

            to_do_list = f.get_todos()

            new_todo = input('Enter the new todo: ') + '\n'
            to_do_list[position] = new_todo #or we can use: 'to_do_list.__setitem__(position, new_todo)'

            f.write_todos(to_do_list)
        except ValueError:
            print('You entered the wrong value')
            continue
        
    elif user_action.startswith('complete'):
        try:
            completed = user_action[9:]

            to_do_list = f.get_todos()

            pos_to_remove = int(completed) - 1
            todo_to_remove = to_do_list[pos_to_remove].strip('\n')
            to_do_list.pop(pos_to_remove)

            f.write_todos(to_do_list)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print('Provide the correct value')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Hey, you entered an unknown command')
    
print('Bye!')

