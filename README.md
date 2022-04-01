# SE Group 06


## Inhaltsverzeichnis

- [Einleitung](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#einleitung)
- [Voraussetzungen](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#einleitung)
- [Installation](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#installation)
- [Erste Schritte](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#erste-schritte)
	- [Verzeichnis auswählen](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#verzeichnis-ausw%C3%A4hlen)
	- [Superuser erstellen](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#superuser-erstellen)
	- [Server starten und Daten migrieren](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#server-starten-und-daten-migrieren)
- [Team](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/tree/main#team)

## Einleitung

Willkommen im GitLab-Verzeichnis der SE Praktikum Gruppe 6. Im Inhaltsverzeichnis oben finden Sie alle Kategorien des README kategorisiert. Im Dokumenten-Verzeichnis
finden Sie alle notwendigen Informationen, Vorbereitungen und Daten, die vor und während der Entwicklung des Projekts entstanden sind. Auch unsere Vorgehensweise ist 
in diesem Verzeichnis festgehalten.

## Voraussetzungen

Um das Projekt lokal installieren und ausführen zu können, müssen folgende Voraussetzungen erfüllt sein. Bitte überprüfen Sie entsprechend vor oder nach dem Kopieren
des GitLab-Verzeichnisses die genannten Voraussetzungen.

Für die reine Ausführung im Browser, müssen folgende Voraussetzungen erfüllt werden:

- Aktuelle Browser: Mozilla Firefox (Version 96+), Google Chrome (Version 96+), Edge (Version 98+), Safari (Version 15+)

Für die Entwicklungsumgebung, müssen zusätzlich folgende Voraussetzungen erfüllt werden:

- [Python 3.10](https://www.python.org/downloads/release/python-3102/)
- [Django 4.0.3](https://www.djangoproject.com/download/)

Zusätzlich kann [PyLint](https://www.pylint.org/) installiert werden, um die Qualität des Codes überprüfen zu können. Für das Begutachten oder Weiterentwickeln des Projekts wird PyLint empfohlen,
wird aber nicht zwingend benötigt und ist entsprechend als eine optionale Empfehlung vermerkt.

## Installation

Um das Projekt in der Entwicklungsumgebung installieren und ausführen zu können, müssen Sie zu Beginn dieses Git-Verzeichnis kopieren. Installieren Sie im Nachhinein
alle notwendigen Frameworks.

Klone per HTTPs:
```
git clone https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06.git
```

Öffnen Sie im Nachhinein das lokale GitLab-Verzeichnis mit Ihrer IDE, vorzugsweise mit [Visual Studio Code](https://visualstudio.microsoft.com/de/) (Microsoft) oder [PyCharm](https://www.jetbrains.com/de-de/pycharm/) (Jetbrains). Installieren Sie dort
die entsprechenden Frameworks und Packages, die benötigt werden, um das Projekt lokal ausführen oder um Anpassungen durchführen zu können.

Django:
```
pip install Django==4.0.3
```

PyLint
```
pip install pylint
```

## Erste Schritte

Damit das Projekt ausgeführt werden kann, müssen gewisse Voraussetzungen erfüllt werden und Daten vorhanden sein. Zu Beginn, nachdem die Installation erfolgreich abgeschlossen worden ist, können wir prüfen, ob alles funktioniert.
Hierfür müssen wir zuerst darauf achten, dass wir im richtigen Verzeichnis sind, wo sich auch die Datei "manage.py" befindet.

### Verzeichnis auswählen

Falls nicht, navigieren wir im Terminal ins richtige Verzeichnis. Wir gehen zum Beispiel davon aus, dass wir uns in folgendem Verzeichnis befinden "C:\Users\(user)\PhpstormProjects\se06\".
Mit folgendem Befehl gelangen wir dann ins richtige Verzeichnis:
```
cd WebsiteDjango
```

### Superuser erstellen

Damit das Login und die Registrierung von neuen Benutzern möglich ist, muss ein Superuser erstellt werden, der die Benutzerrollen ("Groups") anlegt. 
Hierfür gehen wir wie folgt vor:

```
python manage.py createsuperuser
```

Nachdem wir diesen Befehl eingegeben haben, können wir nun ein Benutzernamen, eine E-Mail Adresse (nicht notwendig) und ein Passwort setzen. Diese benötigen wir gleich, um Daten in die Datenbank eintragen zu können.

### Server starten und Daten migrieren

Um den Server starten und auf unser Projekt im Browser zugreifen zu können, geben wir folgenden Befehl im Terminal ein:
```
py -m manage runserver
```
Falls der Befehl erfolgreich ausgeführt sein sollte, wird im Terminal auch die Serveradresse erwähnt, mit der wir das Projekt im Browser aufrufen können. Standardmäßig sollte die Adresse lauten "[http://127.0.0.1:8000/](http://127.0.0.1:8000/)".
Sollte der Server unter der folgenden Adresse aufrufbar sein, kannst du nun in den Adminbereich navigieren: "/admin/"

Melde dich dort mit deinem Superuser-Zugang an und navigiere anschließend auf "Groups". Erstelle dort folgende Rollen: "Student", "Prüfer" und "Dozent". Sollten dir die Datenbanken nicht angezeigt werden, musst du noch bevor du den Server startest folgenden Befehl ausführen:
```
python manage.py migrate
```


## Team

Das Team besteht aus acht Mitgliedern. Die Aufgaben für die jeweiligen Mitglieder werden regelmäßig - siehe [Organisatorisches Konzept](https://gitlab.rlp.net/sw-eng-internship-2022/group-6/se06/-/blob/main/Dokumente/Organisatorisches_Konzept.pdf), verteilt.
Das Team besteht aus folgenden Mitgliedern: 

- Andreas Krieger
- Nico Thomas Kunze
- Gianluca Lefebvre
- Daniel Britschak
- Theo Stempel-Hauburger
- Ricardo Pacilli
- Hannes Bernhard Schott
- Can Tarhan
