from tkinter import *
from tkinter import ttk


class MestForPengene:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui

    def find_coffies(self):
        """Brukeren skal kunne få skrevet ut en liste over hvilke kaffer som har flest gjenomsnittspoeng per krone.
        Listen skal inneholde brennerinavn, kaffenavn, pris og gjennomsnittsscore for hver kaffe.
        Listen skal være sortert."""

        self.database.execute("SELECT Kaffebrenneri.Navn, Kaffe.Navn, Kaffe.Kilopris, AVG(Kaffesmaking.AntallPoeng) AS GJSN_POENG\
        FROM (Kaffe INNER JOIN Kaffebrenneri USING(KaffebrenneriID)) INNER JOIN Kaffesmaking USING (KaffeID)\
        GROUP BY KaffeID\
        ORDER BY (GJSN_POENG / Kaffe.Kilopris) DESC")

        res = self.database.fetchall()
        self.database.commit()

        self.root.geometry("800x300")
        page = Frame(self.root)
        page.pack()
        self.gui.navbar(page)
        text1 = Label(self.root, text="Her er informasjon om hvilke kaffer som gir mest verdi for pengene: \n").pack()

        tree = ttk.Treeview(self.root, column=("Navn på kaffebrenneri", "Navn på kaffe", "Kilopris", "Gjsn poeng"), show='headings', height=len(res))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Navn på kaffebrenneri")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Navn på kaffe")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Kilopris")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Gjsn poeng")

        for tup in res:
            tree.insert('', 'end', text="", values=tup)

        tree.pack()
