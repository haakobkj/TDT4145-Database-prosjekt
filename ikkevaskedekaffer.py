from tkinter import *
from tkinter import ttk


class IkkeVaskedekaffer:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui

    def print_coffees(self):
        """Brukeren skal kunne få skrevet ut en liste over kaffer som ikke er vaskede og som er fra
        Rwanda eler Colombia. Dette skal skrives ut i en tabell som inneholder brennerinavn og kaffenavn
        """

        self.database.execute("SELECT Kaffebrenneri.Navn, Kaffe.Navn\
                FROM (Kaffe INNER JOIN Kaffebrenneri USING(KaffebrenneriID)) INNER JOIN Kaffeparti USING(KaffepartiID)\
                INNER JOIN Gaard USING(GaardsID) INNER JOIN RegionILand USING(Region)\
                INNER JOIN Foredlingsmetode USING(ForedlingsmetodeID)\
                WHERE (RegionILand.Land LIKE 'Rwanda' OR RegionILand.Land LIKE 'Colombia')\
                AND (Foredlingsmetode.Navn NOT LIKE 'vask%' OR Foredlingsmetode.Beskrivelse NOT LIKE 'vask%')")

        res = self.database.fetchall()
        self.database.commit()

        self.root.geometry("800x300")
        page = Frame(self.root)
        page.pack()
        self.gui.navbar(page)
        text1 = Label(self.root, text="Her er kaffer som er fra Rwanda eller Colombia og som ikke er vaskede: \n").pack()

        tree = ttk.Treeview(self.root, column=("Navn på kaffebrenneri", "Navn på kaffe"), show='headings', height=len(res))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Navn på kaffebrenneri")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Navn på kaffe")


        for tup in res:
            tree.insert('', 'end', text="", values=tup)

        tree.pack()



