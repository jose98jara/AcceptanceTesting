import pytest
from todo_list import TodoList, Task

@pytest.fixture
def todo_list():
    return TodoList()

def test_add_task(todo_list):
    todo_list.add_task("Buy groceries")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].name == "Buy groceries"

def test_mark_task_completed(todo_list):
    todo_list.add_task("Buy groceries")
    todo_list.mark_task_completed("Buy groceries")
    assert todo_list.tasks[0].status == "Completed"

def test_clear_tasks(todo_list):
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    todo_list.clear_tasks()
    assert len(todo_list.tasks) == 0

def test_list_tasks(todo_list):
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    tasks = todo_list.list_tasks()
    assert "Buy groceries" in tasks
    assert "Pay bills" in tasks
