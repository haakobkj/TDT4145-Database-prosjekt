from tkinter import *
from tkinter import ttk


class KaffeBeskrevetMed:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui
        self.ord = None
        self.ord_entry = None

    def sok_etter_ord_i_beskrivelse(self):
        """En bruker søker etter kaffer som er blitt beskrevet med strengen fra input
        enten av brukere eller brennerier. Brukeren skal få tilbake en liste med
        brennerinavn og kaffenavn."""

        self.root.geometry("800x300")
        page = Frame(self.root)
        page.pack()
        self.gui.navbar(page)
        text1 = Label(self.root, text="Her kan du søke på kaffer beskrevet av et spesielt ord").pack()
        text1 = Label(self.root, text="Søk etter:").pack()
        self.ord_entry = Entry(self.root)
        self.ord_entry.pack()
        button = Button(self.root, text="Submit", command=lambda : self.onClick()).pack()


    def onClick(self):
        """Søker etter kaffer beskrevet med strengen som kommer fra input fra brukeren.
        Søker både i beskrivelsen til kaffen og smaksnotater fra kaffesmakinger for den gitte kaffen"""

        self.ord = self.ord_entry.get()

        self.database.execute("SELECT DISTINCT Kaffebrenneri.Navn, Kaffe.Navn\
                              FROM (Kaffebrenneri INNER JOIN Kaffe USING (KaffebrenneriID))\
                              LEFT OUTER JOIN Kaffesmaking USING (KaffeID)\
                              WHERE Kaffe.Beskrivelse LIKE ? OR Kaffesmaking.Smaksnotater LIKE ?", ('%'+self.ord+'%', '%'+self.ord+'%'))

        res = self.database.fetchall()
        text1 = Label(self.root, text="Her er kaffer som inneholder " + self.ord + ": \n").pack()

        tree = ttk.Treeview(self.root, column=("Navn på kaffebrenneri", "Navn på kaffe"), show='headings', height=len(res))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Navn på kaffebrenneri")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Navn på kaffe")

        for tup in res:
            tree.insert('', 'end', text="", values=tup)

        tree.pack()
