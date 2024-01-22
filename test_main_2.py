from functions import get_todos
from functions import write_todos
from functions import current_time

def test_get_todos():
    todo = get_todos()
    todo.append("testing")
    assert len(todo) >= 1

def test_write_todos():
    todo = get_todos()
    todo.append("testing")
    assert "testing" in write_todos(todo)

def test_current_time():
    todo_time = current_time()
    assert type(todo_time) == str



