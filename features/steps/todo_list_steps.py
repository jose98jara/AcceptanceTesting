from behave import given, when, then
from todo_list import TodoList  # Suponiendo que tienes el archivo `todo_list.py`

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = TodoList()

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    tasks = context.todo_list.list_tasks()
    assert any(task_name in task for task in tasks)

@when('the user lists all tasks')
def step_impl(context):
    context.tasks = context.todo_list.list_tasks()

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = TodoList()
    for row in context.table:
        task_name = row['Task']
        context.todo_list.add_task(task_name)

@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    context.todo_list.mark_task_completed(task_name)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@then('the output should contain')
def step_impl(context):
    # Extraemos las tareas esperadas de la tabla, sin importar el estado
    expected_tasks = [row['Task'].strip() for row in context.table]
    
    # Extraemos solo el nombre de las tareas reales, eliminando el estado "(Pending)"
    actual_tasks = [task.split(" (")[0].strip() for task in context.tasks]
    
    # Comparamos las tareas esperadas con las tareas reales
    assert sorted(expected_tasks) == sorted(actual_tasks), f"Expected tasks: {expected_tasks}, but got: {actual_tasks}"


@then('the to-do list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    task_status = None
    for task in context.todo_list.tasks:
        if task.name == task_name:
            task_status = task.status
    assert task_status == "Completed"

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0
