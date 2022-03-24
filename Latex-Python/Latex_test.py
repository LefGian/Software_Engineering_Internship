
class Aufgabe:
    def __init__(self, name: str, aufgabenstellung: str, loesung: str, username: str, schwierigkeit: int, zeit: int, themengebiet: str):
        self.name = name
        self.aufgabenstellung = aufgabenstellung
        self.loesung = loesung
        self.username = username    # Name as string of the User object
        self.schwierigkeit = schwierigkeit
        self.zeit = zeit    # time in minutes
        self.themengebiet = themengebiet


def toLatex(aufgabe_arr, type: int, loesung: bool):
    """
    par:    aufgabe_arr,  Array of objects of Class Aufgabe containing important Information to be put to Latex
    par:    type,   Integer telling wich type of file should be generated.
        0 -> Klausur    --> Klausur wird erzeugt, falls loesung==true werden die Loesungen draufgeschrieben
        1 -> Uebungsblatt   --> Uebungsblatt wird erzeugt, falls loesung==true werden die Loesungen draufgeschrieben
    par:    loesung,    sollen die Musterloesungen draufgeschieben wreden ?
    returns:    Tuple of LatexFile and .pdf File -> (latexfile, pdf)
    """
    with open("questions.tex", "w") as latex:
        latex.write("\\begin{questions}\n")
        for aufgabe in aufgabe_arr:
            latex.write(aufgabe.name + "\n")
            latex.write(aufgabe.aufgabenstellung + "\n")
        if loesung:
            latex.write(aufgabe.loesung + "\n")
        latex.write("\\pagebreak\n")
        latex.write("\\end{questions}\n")
    return latex