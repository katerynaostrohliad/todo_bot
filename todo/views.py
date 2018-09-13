from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer
from todo.database.todo import insert_todo, delete_todo, get_one_todo, get_task_with_user
from todo.database.user import add_user, delete_user, get_user


#/Welcome
class Welcome(APIView):

    def get(self, request): #read info
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        content = (serializer.data, user_serializer.data)
        return Response(content, status=200)

    def post(self, request):#create new ones
        payload = request.data
        serializer = TodoSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/UserView
class UserView(APIView):
    def add_user(self, request):
        payload = request.data
        try:
            added_user = add_user(payload)
        except IntegrityError:
            return Response("User already exists")
        return Response(added_user, status=status.HTTP_201_CREATED)

    def delete_user(self, request):
        reporter_id = request.data
        try:
            deleted_user = delete_user(reporter_id)
        except User.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
        return deleted_user

    def get_user(self, request):
        reporter_id = request.data
        try:
            user = get_user(reporter_id)
        except User.DoesNotExist:
            return None
        return user

#/TodoView
class TodoView(APIView):
    def insert_todo(self, request):
        payload = request.data
        todo = insert_todo(payload)
        return Response(todo, status=status.HTTP_201_CREATED)

    def delete_todo(self, request):
        task_id = request.data
        try:
            deleted_todo = delete_todo(task_id)
        except Todo.DoesNotExist:
            return Response("Task does not exist", status=status.HTTP_400_BAD_REQUEST)
        return deleted_todo

    def get_task_with_user(self, request):
        reporter_id = request.data
        try:
            get_task = get_task_with_user(reporter_id)
        except User.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
        return get_task

    def get_one_todo(self, request):
        task_id = request.data
        try:
            task = get_one_todo(task_id)
        except Todo.DoesNotExist:
            return Response("Task does not exist", status=status.HTTP_400_BAD_REQUEST)#is it better to
            # return none or bad request
        return task




