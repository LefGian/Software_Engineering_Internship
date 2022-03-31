import random
from django.contrib.auth.models import User, Group
from startsite.models import *


def toLatex_html(aufgabe_arr, loesung_anzeigen: bool):
    with open("home/templates/home/questions.html", "w", encoding="utf-8") as latex:
        latex.write('<pre>\n')
        latex.write("\\begin{questions}\n")
        for aufgabe in aufgabe_arr:
            latex.write("\Question{0}" + "{" + f"{aufgabe.name}({aufgabe.themengebiet})" + "}\n")
            latex.write(aufgabe.aufgabenstellung + "\n")
            if loesung_anzeigen:
                latex.write("\\begin{solution}\n")
                latex.write(aufgabe.loesung + "\n")
                latex.write("\\end{solution}\n")
            latex.write("\\pagebreak\n")
        latex.write("\\end{questions}\n")
        latex.write('</pre>\n')
        latex.close()
    return latex


def toLatex(aufgabe_arr, loesung_anzeigen: bool):
    with open("questions.tex", "w", encoding="utf-8") as latex:
        latex.write("\\begin{questions}\n")
        for aufgabe in aufgabe_arr:
            latex.write("\Question{0}" + "{" + f"{aufgabe.name}({aufgabe.themengebiet})" + "}\n")
            latex.write(aufgabe.aufgabenstellung + "\n")
            if loesung_anzeigen:
                latex.write("\\begin{solution}\n")
                latex.write(aufgabe.loesung + "\n")
                latex.write("\\end{solution}\n")
            latex.write("\\pagebreak\n")
        latex.write("\\end{questions}\n")
        latex.close()
    return latex


def file_to_str(filename: str):
    with open(filename, 'r') as file:
        data = file.read()
    return data


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


def get_fachgebiet():
    fachgebiete = Fachgebiet.objects.all()

    return fachgebiete


def get_fachgebiet_name():
    fachgebiete = Fachgebiet.objects.all()

    fachgebiete_name = [i.name for i in fachgebiete]

    return fachgebiete_name


def get_fachgebiet_by_id(id):
    if not id:
        return None
    return Fachgebiet.objects.get(id=id)


def get_themengebiet(fachgebietID: int):
    """
    Use this to gather all objects of Themengebiete that belong to the Fachgebiet

    :param FachgebietID: ID(int) of Fachgebiet that filters the Themengebiete by Fachgebiet. Can be None
    :return: List of Objects of all Themengebiet names matching the filters
    """

    fachgebiet = Fachgebiet.objects.get(id=fachgebietID)

    themengebiete = Themengebiet.objects.filter(fachgebiet=fachgebiet)

    return themengebiete


def get_themengebiet_name(fachgebietID: int):
    """
    Use this to gather all names of Themengebiete that belong to the Fachgebiet

    :param FachgebietID: ID(int) of Fachgebiet that filters the Themengebiete by Fachgebiet. Can be None
    :return: List of strings of all Themengebiet names matching the filters
    """

    fachgebiet = Fachgebiet.objects.get(id=fachgebietID)

    themengebiete = Themengebiet.objects.filter(fachgebiet=fachgebiet)

    themengebiete_name = [i.name for i in themengebiete]

    return themengebiete_name


def get_themengebiet_by_id(id):
    return Themengebiet.objects.get(id=id)


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


def filter_aufgabe(themengebietID: int, schwierigkeit: int, zeit: int):
    """
    Use this to gather all filtered tasks informations for sheets/exam latex.
    Fields can be None.

    :param themengebietID: ID(int) of Themengebiet that filters the tasks by topic. Can be None
    :param schwierigkeit: int that filters the tasks by difficulty. Can be None
    :param zeit: int that filters the tasks by time. Can be None
    :return: QuerySet(List of Objects) of all tasks matching the filters
    """

    aufgaben = Aufgabe.objects.all()
    aufgaben_gefiltert = []

    try:
        themengebiet_record = Themengebiet.objects.get(id=themengebietID)
    except:
        print("Why u do dis???")
        return []

    if themengebietID is not None:
        aufgaben = aufgaben.filter(themengebiet_id=themengebiet_record.id)

    if schwierigkeit is not None and schwierigkeit != 0:
        aufgaben = aufgaben.filter(schwierigkeit=schwierigkeit)

    if zeit is not None and zeit != 0:
        aufgaben = aufgaben.filter(zeit=zeit)

    for aufgabe in aufgaben:
        aufgaben_gefiltert.append(aufgabe)
    return aufgaben_gefiltert


def filter_aufgabe_name(themengebietID: int, schwierigkeit: int, zeit: int):
    """
    Use this to gather all filtered tasks names to display at site.
    Fields can be None.

    :param themengebietID: ID(int) of Themengebiet that filters the tasks by topic. Can be None
    :param schwierigkeit: int that filters the tasks by difficulty. Can be None
    :param zeit: int that filters the tasks by time. Can be None
    :return: List of strings of all task names matching the filters
    """

    aufgaben = Aufgabe.objects.all()

    try:
        themengebiet_record = Themengebiet.objects.get(id=themengebietID)
    except:
        return []

    if themengebietID is not None:
        aufgaben = aufgaben.filter(themengebiet_id=themengebiet_record.id)

    if schwierigkeit is not None:
        aufgaben = aufgaben.filter(schwierigkeit=schwierigkeit)

    if zeit is not None and zeit != 0:
        aufgaben = aufgaben.filter(zeit=zeit)

    aufgaben_name = [i.name for i in aufgaben]

    return aufgaben_name


def get_aufgabe_by_id(id):
    return Aufgabe.objects.get(id=id)


def add_aufgabe(name: str, aufgabenstellung: str, loesung: str, user: User, schwierigkeit: int, zeit: int,
                themengebietID: int):
    """
    Use this to add a Aufgabe.

    TOD0: Add field "Punkte" to database-table "Aufgabe"

    :param name: String to define the name of Aufgabe
    :param aufgabenstellung: String to define the aufgabenstellung of Aufgabe
    :param loesung: String to define the loesung of Aufgabe
    :param user: User to define the designer of the Aufgabe. Should be the current user
    :param schwierigkeit: int to define the schwierigkeit of Aufgabe
    :param zeit: int to define the zeit of Aufgabe
    :param themengebietID: ID(int) of Themengebiet to define the themengebiet of Aufgabe
    :return: 0 on success, -1 on failure
    """

    try:
        themengebiet_record = Themengebiet.objects.get(id=themengebietID)

        aufgabe = Aufgabe(name=name, aufgabenstellung=aufgabenstellung, loesung=loesung, user=user,
                          schwierigkeit=schwierigkeit, zeit=zeit, themengebiet=themengebiet_record)

        aufgabe.save()

        return 0
    except:
        return -1


def check_if_value_is_set(value):
    if not value:
        return 0
    else:
        return int(value)


def create_exam(themengebietID: int, schwierigkeit: int, zeit: int):
    aufgaben = [i for i in
                Aufgabe.objects.filter(themengebiet_id=themengebietID, schwierigkeit=schwierigkeit, zeit__lt=zeit)]
    random.shuffle(aufgaben)
    time = zeit
    exam = []

    for aufgabe in aufgaben:
        if aufgabe.zeit <= time:
            exam.append(aufgabe)
            time = time - int(aufgabe.zeit)

    return exam


def apply_filter(request):
    topic_id = check_if_value_is_set(request.POST['jgu-topic-filter'])
    topic = get_themengebiet_by_id(topic_id)
    time = check_if_value_is_set(request.POST['jgu-time-filter'])
    difficulty = check_if_value_is_set(request.POST['jgu-level-filter'])
    tasks = filter_aufgabe(topic_id, difficulty, time)

    selected_time = time
    selected_difficulty = difficulty

    return tasks, selected_time, selected_difficulty, topic


def get_filter_attributes(request):
    topic = check_if_value_is_set(request.POST['jgu-topic-filter'])
    difficulty = check_if_value_is_set(request.POST['jgu-level-filter'])
    time = check_if_value_is_set(request.POST['jgu-time-filter'])

    return topic, difficulty, time


def init_aufgabe():
    themengebiete = Themengebiet.objects.all()
    schwierigkeit = 1
    zeit = 5

    for i in themengebiete:
        for j in range(100):
            a = Aufgabe(name=f"{i.name} Aufgabe {j}", aufgabenstellung=f"{j} * {j}", loesung=f"{j * j}",
                        schwierigkeit=schwierigkeit, zeit=zeit, themengebiet_id=i.id, user=User.objects.get(id=1))
            a.save()

            schwierigkeit = (schwierigkeit % 7) + 1
            zeit = (zeit % 25) + 5
