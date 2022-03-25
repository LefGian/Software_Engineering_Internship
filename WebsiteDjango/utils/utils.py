from django.contrib.auth.models import User, Group
# from ... import Aufgabe muss noch importiert werden



def set_group(user: User, groupname: str):
    """
    Use this to set users group.

    :param user: user whose groups will be set
    :param groupname: string of group that will be assigned to user. e.g. "Student", "Dozent", "Prüfender"
    :return: void
    """

    group_id = Group.objects.get(name=groupname).id
    user.groups.add(group_id)


def get_group(user: User):
    """
    Use this to get users groups as list of strings.

    :param user: user whose groups will be returned
    :return: list of groupnames as strings
    """

    groups = user.groups.all()
    group_names = [i.name for i in groups]

    return group_names


def update_user(user: User, username: str, first_name: str, last_name: str, new_password: str):
    """
    Use this to update users information. No field should be None.

    :param user: user that will be updated
    :param username: new username as string
    :param first_name: new first_name as string
    :param last_name: new last_name as string
    :param new_password: new password as string
    :return: void
    """
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.set_password(new_password)

    user.save()


def filter_aufgabe(themengebiet: str, schwierigkeit: int, zeit: int):
    """
    Use this to gather all filtered tasks informations for sheets/exam latex.
    Fields can be None.

    :param themengebiet: string that filters the tasks by topic. Can be None
    :param schwierigkeit: int that filters the tasks by difficulty. Can be None
    :param zeit: int that filters the tasks by time. Can be None
    :return: QuerySet of all tasks matching the filters
    """

    aufgaben = Aufgabe.objects.all()

    if themengebiet is not None:
        aufgaben = aufgaben.filter(themengebiet=themengebiet)

    if schwierigkeit is not None:
        aufgaben = aufgaben.filter(schwierigkeit=schwierigkeit)

    if zeit is not None:
        aufgaben = aufgaben.filter(zeit=zeit)


    return aufgaben


def filter_aufgabe_name(themengebiet: str, schwierigkeit: int, zeit: int):
    """
    Use this to gather all filtered tasks names to display at site.
    Fields can be None.

    :param themengebiet: string that filters the tasks by topic. Can be None
    :param schwierigkeit: int that filters the tasks by difficulty. Can be None
    :param zeit: int that filters the tasks by time. Can be None
    :return: List of strings of all task names matching the filters
    """

    aufgaben = Aufgabe.objects.all()

    if themengebiet is not None:
        aufgaben = aufgaben.filter(themengebiet=themengebiet)

    if schwierigkeit is not None:
        aufgaben = aufgaben.filter(schwierigkeit=schwierigkeit)

    if zeit is not None:
        aufgaben = aufgaben.filter(zeit=zeit)


    aufgaben_name = [i.name for i in aufgaben]

    return aufgaben_name



def add_aufgabe(name: str, aufgabenstellung: str, loesung: str, user: User, schwierigkeit: int, zeit: int,
                themengebiet: str):
    """
    Use this to add a Aufgabe.

    TOD0: Add field "Punkte" to database-table "Aufgabe"

    :param name: String to define the name of Aufgabe
    :param aufgabenstellung: String to define the aufgabenstellung of Aufgabe
    :param loesung: String to define the loesung of Aufgabe
    :param user: User to define the designer of the Aufgabe. Should be the current user
    :param schwierigkeit: int to define the schwierigkeit of Aufgabe
    :param zeit: int to define the zeit of Aufgabe
    :param themengebiet: String to define the themengebiet of Aufgabe
    :return:
    """

    try:
        aufgabe = Aufgabe(name=name, aufgabenstellung=aufgabenstellung, loesung=loesung, user=user,
                      schwierigkeit=schwierigkeit, zeit=zeit, themengebiet=themengebiet)

        aufgabe.save()
    
        return 0
    except:
        return -1

