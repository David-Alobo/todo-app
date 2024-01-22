while True:
    user_action = input('Type add, show, complete, edit or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            to_do = input('Enter a todo: ') + '\n'

            with open(r"C:\codebase\my_files\my_practice\todo app\todo.txt", 'r') as file:
                to_do_list = file.readlines()
                
                to_do_list.append(to_do.title())

            with open(r"C:\codebase\my_files\my_practice\todo app\todo.txt", 'w') as file:
                file = file.writelines(to_do_list)          

        case 'show':
            with open(r"C:\codebase\my_files\my_practice\todo app\todo.txt", 'r') as file:
                to_do_list = file.readlines()

                new_to_do_list = []

                for i in to_do_list:
                    new_item = i.strip('\n')
                    new_to_do_list.append(new_item) 

                for index, item in enumerate(new_to_do_list):
                    print(f'{index + 1}. {item}')

        case 'edit':
            number = int(input('Enter the number of the todo: '))
            position = number - 1

            with open(r"C:\codebase\my_files\my_practice\todo app\todo.txt", 'r') as file:
                to_do_list = file.readlines()

            new_todo = input('Enter the new todo: ') + '\n'
            to_do_list[position] = new_todo #or we can use: 'to_do_list.__setitem__(position, new_todo)'

            with open(r"C:\codebase\my_files\my_practice\todo app\todo.txt", 'w') as file:
                file = file.writelines(to_do_list)

            # to_be_edited = to_do_list[position] # or we can use: 'to_do_list.__getitem__(position)'
            # print('Confirm value to be edited: {}'.format(to_be_edited))
            
            # print(new_todo)
            
        case 'complete':
            completed = input('Enter todo completed: ')
            to_do_list.remove(completed)
        case 'exit':
            break
        case _: #or 'whatever' can be used in place of underscore
            print('Hey, you entered an unknown command')
    
print('Bye!')

