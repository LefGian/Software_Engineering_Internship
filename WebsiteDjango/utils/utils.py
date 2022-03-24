from django.contrib.auth.models import User, Group
# from ... import Aufgabe muss noch importiert werden



def set_group(user: User, groupname: str):
    group_id = Group.objects.get(name=groupname).id
    user.groups.add(group_id)

def get_group(user: User):
    groups = user.groups.all()
    group_names = [i.name for i in groups]

    return group_names

def update_user(user: User, username: str, first_name: str, last_name: str, new_password: str):
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.set_password(new_password)
    user.save()