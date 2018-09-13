
from todo.models import User
from todo.serializers import UserSerializer


def add_user(payload, user):
    #adds user to the db
    new_user = User(
        first_name=payload["first_name"],
        last_name=payload["last_name"],
        reporter=user
    )
    new_user.save()#deserializes new_user and adds to db
    serialized = UserSerializer(new_user)#to json
    return serialized.data


def delete_user(reporter_id):
    user = User.objects.filter(id=reporter_id).delete()
    if user[0] == 0:
        return None
    return user #returns db object


def get_user(reporter_id):
    try:
        user = User.objects.get(pk=reporter_id)
    except User.DoesNotExist:
        return None
    return user #gets a user from the table by id
