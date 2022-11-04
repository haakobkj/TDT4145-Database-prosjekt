import tkinter as tk


class LoginPage:

    def __init__(self, database, root, gui):
        self.database = database
        self.root = root
        self.gui = gui
        self.epost = None
        self.passord = None
        self.username_entry = None
        self.password_entry = None

    def loginpage(self):
        """Gir brukeren mulighet til å logge inn i appklikasjonen."""
        self.root.geometry("800x300")
        page = tk.Frame(self.root)
        page.pack()
        text = tk.Label(self.root, text="Velkommen til KaffeDB!").pack()
        label1 = tk.Label(self.root, text="Epost").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        label2 = tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()
        button = tk.Button(self.root, text="Submit", command=lambda : self.on_click()).pack()

    def on_click(self):
        """Kjøres når man klikker på Submit. Sjekker om eposten og passordet stemmer med de som er i databasen og
        logger inn hvis de er riktig."""

        try:
            self.epost = self.username_entry.get()
            self.passord = self.password_entry.get()

            self.database.execute("SELECT Epost FROM Bruker;")
            eposter = self.database.fetchall()
            eposter = [x[0] for x in eposter]
            if self.epost not in eposter:
                raise Exception("Eposten eksisterer ikke i databasen.")

            self.database.execute("SELECT Passord FROM Bruker WHERE Epost = ?", (self.epost,))
            brukers_passord = "".join(self.database.fetchone())
            if not self.passord == brukers_passord:
                raise Exception("Feil passord")

            self.database.commit()

            self.gui.logged_in = self.epost
            self.gui.changepage(1)
        except Exception:
            text = tk.Label(self.root, text="Feil passord eller brukernavn", fg="red")
            text.pack()
