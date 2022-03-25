"""
python script for generating a .tex file of different exercises from the database
"""


class Aufgabe:
    """
    class for exercise objects with important attributes to generate .tex file
    """

    def __init__(self, name: str, aufgabenstellung: str, loesung: str, username: str,
                 schwierigkeit: int, zeit: int, themengebiet: str):
        self.name = name
        self.aufgabenstellung = aufgabenstellung
        self.loesung = loesung
        self.username = username  # Name as string of the User object
        self.schwierigkeit = schwierigkeit
        self.zeit = zeit  # time in minutes
        self.themengebiet = themengebiet


def to_latex(aufgabe_arr, loesung: bool):
    """
    par: aufgabe_arr,  Array of objects of Class Aufgabe to be put in .tex file
    par:    loesung, bool if True: solution of the exercise will be in .tex file
    returns: .tex file
    """
    with open("questions.tex", "w", encoding="utf-8") as latex:
        latex.write("\\begin{questions}\n")
        for aufgabe in aufgabe_arr:
            latex.write(aufgabe.name + "\n")
            latex.write(aufgabe.aufgabenstellung + "\n")
        if loesung:
            latex.write(aufgabe.loesung + "\n")
        latex.write("\\pagebreak\n")
        latex.write("\\end{questions}\n")
    return latex
