import tkinter as tk
from datetime import date


class Kaffesmaking:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui
        self.kaffenavn = None
        self.poeng = None
        self.brenneri = None
        self.brenedato = None
        self.smaksnotater = None
        self.kaffenavn_entry = None
        self.poeng_entry = None
        self.brenneri_entry = None
        self.brenedato_entry = None
        self.smaksnotater_entry = None

    def kaffesmaking_page(self):
        """ Lager komponentene for å ta inn data fra brukeren."""

        self.root.geometry("800x300")
        page = tk.Frame(self.root)
        page.pack()
        self.gui.navbar(page)
        text = tk.Label(self.root, text="Her kan du legge inn en ny kaffesmaking!").pack()
        label1 = tk.Label(self.root, text="Kaffe:").pack()
        self.kaffenavn_entry = tk.Entry(self.root)
        self.kaffenavn_entry.pack()
        label2 = tk.Label(self.root, text="Poeng:").pack()
        self.poeng_entry = tk.Entry(self.root)
        self.poeng_entry.pack()
        label3 = tk.Label(self.root, text="Brenneri:").pack()
        self.brenneri_entry = tk.Entry(self.root)
        self.brenneri_entry.pack()
        label4 = tk.Label(self.root, text="Brennedato (dd/mm/yyyy):").pack()
        self.brenedato_entry = tk.Entry(self.root)
        self.brenedato_entry.pack()
        label5 = tk.Label(self.root, text="Smaksnotater:").pack()
        self.smaksnotater_entry = tk.Entry(self.root)
        self.smaksnotater_entry.pack()
        button = tk.Button(self.root, text="Registrer ny kaffesmaking", command=lambda : self.on_click()).pack()

    def on_click(self):
        """Setter inn dataen fra brukeren i databasen når brukeren trykker på Submit"""

        try:
            self.kaffenavn = self.kaffenavn_entry.get()
            self.poeng = self.poeng_entry.get()
            self.brenneri = self.brenneri_entry.get()
            self.brenedato = self.brenedato_entry.get()
            self.smaksnotater = self.smaksnotater_entry.get()
            self.database.execute("SELECT BrukerID FROM Bruker WHERE Epost = ?", (self.gui.logged_in,))
            bruker = self.database.fetchone()
            bruker_id = bruker[0]

            today = date.today()
            time = today.strftime("%d/%m/%Y")

            self.kaffenavn = self.kaffenavn_entry.get()
            self.brenneri = self.brenneri_entry.get()
            self.smaksnotater = self.smaksnotater_entry.get()
            self.poeng = self.poeng_entry.get()

            self.database.execute("SELECT KaffeID \
                                   FROM Kaffe INNER JOIN Kaffebrenneri USING (KaffebrenneriID)\
                                   WHERE Kaffe.Navn = ? AND Kaffebrenneri.Navn = ? AND Dato = ?", (self.kaffenavn, self.brenneri, self.brenedato))
            temp = self.database.fetchone()
            kaffe_id = temp[0]

            sqlite_insert_with_param = """INSERT INTO Kaffesmaking
                                      (Smaksnotater, AntallPoeng, Smaksdato, BrukerID, KaffeID) 
                                      VALUES (?, ?, ?, ?,?);"""

            data_tuple = (self.smaksnotater, self.poeng, time, bruker_id, kaffe_id)

            self.database.execute(sqlite_insert_with_param, data_tuple)

            self.database.commit()
            text = tk.Label(self.root, text="Kaffesmakingen ble lagt til", fg="green").pack()
        except:
            text = tk.Label(self.root, text="Noe gikk galt, kaffesmakingen ble ikke lagt til", fg="red").pack()
