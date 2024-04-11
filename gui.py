import functions
import PySimpleGUI as sg
import time

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text('To_Do App')

add_button = sg.Button(size=2, 
                       image_source="add.png", 
                       tooltip='Add Item', 
                       mouseover_colors='LightGray', 
                       key='Add')

input_box = sg.InputText(tooltip='Enter todo', key='todo')

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button(size=2,
                            image_source="complete.png",
                            tooltip="Complete",
                            key="Complete")
exit_button = sg.Button(size=2,
                            image_source="exit.png",
                            tooltip="Exit",
                            key="Exit")

window = sg.Window('My To-Do App', 
                   layout=[[clock,]
                            [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button]
                           [exit_button]],
                   font=('Helvetica', 20))
window.read()
window.close()

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todos'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['tofos'.update](values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup('Please select an item first', font=('Helvetica', 20))
        
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todos'].update(value="")
            except IndexError:
                sg.Popup('Please select an item first', font=('Helvetica', 20))


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'[0]])
        
        case sg.WIN_CLOSED:
            break

window.close()


