from tkinter import *
from tkinter import ttk
from datetime import date


class FlestUnikeKaffesmakinger:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui

    def flest_unike_kaffesmakinger(self):
        """En bruker skal kunne få skrevet ut en liste over hvilke brukere som
        har smakt flest unike kaffer så langt i år, sortert synkende. Listen skal
        inneholde brukernes fulle navn og antallet kaffer de har smakt."""

        year = '%' + str(date.today().year)

        self.database.execute("SELECT Bruker.Navn, COUNT (DISTINCT Kaffesmaking.KaffeID) as Kaffesmakinger\
                FROM Bruker INNER JOIN Kaffesmaking USING (BrukerID)\
                WHERE Kaffesmaking.Smaksdato LIKE ?\
                GROUP BY Bruker.Navn\
                ORDER BY Kaffesmakinger DESC", (year,))

        res = self.database.fetchall()
        self.database.commit()

        self.root.geometry("800x300")
        page = Frame(self.root)
        page.pack()
        self.gui.navbar(page)
        text1 = Label(self.root, text="Her er informasjon om hvem som har smakt flest unike kaffer i år: \n").pack()

        tree = ttk.Treeview(self.root, column=("Navn", "Antall kaffesmakinger"), show='headings', height=len(res))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Navn")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Antall kaffesmakinger")

        for tup in res:
            tree.insert('', 'end', text="", values=tup)

        tree.pack()
