from todo.models import Todo
from todo.serializers import TodoSerializer


def insert_todo(payload, user):
    new_todo = Todo(
        tasks=payload["tasks"],
        period=payload['time_for_accomplishing'],
        time_of_accomplishing=payload['time_of_accomplishing'],
        reporter=user,
    )
    new_todo.save()
    serialized = TodoSerializer(new_todo)
    return serialized.data


def delete_todo(task):
    todo = Todo.objects.filter(id=task).delete()
    if task[0] == 0:
        return None
    return todo


def get_task_with_user(reporter_id):
    try:
        tasks = Todo.objects.get(id=reporter_id, many=True)
    except Todo.DoesNotExist:
        return None
    serialized = TodoSerializer(tasks)
    return serialized.data


def get_one_todo(task_id):
    try:
        task_id = Todo.objects.get(id=task_id)
    except Todo.DoesNotExist:
        return None
    serialized = TodoSerializer(task_id)
    return serialized.data


def check_time(time_of_accomplishing):
    if time_of_accomplishing.is_valid:
        return "Success"



