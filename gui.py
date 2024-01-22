import functions
import PySimpleGUI as sg

label = sg.Text('To_Do App')
add_button = sg.Button('Add')
input_box = sg.InputText(tooltip='Enter todo')

window = sg.Window('My To-Do App', layout=[[label],[input_box, add_button]])
window.read()
window.close()
