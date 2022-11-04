import tkinter as tk
from database import Database
import login
import kaffesmaking
import flestunikekaffesmakinger
import mestforpengene
import kaffebeskrevetmed
import ikkevaskedekaffer

# Globale variabler
root = tk.Tk()
logged_in = None


class GUI:

    def __init__(self, database):
        self.database = database

    def changepage(self, userstory):
        """Endrer mellom sidene i navbaren"""

        for widget in root.winfo_children():
            widget.destroy()
        if userstory == 1:
            ks = kaffesmaking.Kaffesmaking(self.database, root, self)
            ks.kaffesmaking_page()
        elif userstory == 2:
            fuk = flestunikekaffesmakinger.FlestUnikeKaffesmakinger(self.database, root, self)
            fuk.flest_unike_kaffesmakinger()
        elif userstory == 3:
            mfp = mestforpengene.MestForPengene(self.database, root, self)
            mfp.find_coffies()
        elif userstory == 4:
            sok = kaffebeskrevetmed.KaffeBeskrevetMed(self.database, root, self)
            sok.sok_etter_ord_i_beskrivelse()
        elif userstory == 5:
            ikke_vasket = ikkevaskedekaffer.IkkeVaskedekaffer(self.database, root, self)
            ikke_vasket.print_coffees()
        else:
            raise ValueError("Illegal state")

    def navbar(self, page):
        """Viser navbar øverst i appen"""

        tk.Button(page, text="Registrer ny kaffesmaking", command=lambda: self.changepage(1)).grid(row=0, column=0)
        tk.Button(page, text="Flest unike kaffesmakinger", command=lambda: self.changepage(2)).grid(row=0, column=1)
        tk.Button(page, text="Mest for pengene", command=lambda: self.changepage(3)).grid(row=0, column=2)
        tk.Button(page, text="Søk", command=lambda: self.changepage(4)).grid(row=0, column=3)
        tk.Button(page, text="Ikke vaskede kaffer", command=lambda: self.changepage(5)).grid(row=0, column=4)


def main():
    """Funksjon som kjører appen"""

    root.title("KaffeDB")
    db = Database("KaffeDB.db")
    db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    res = db.fetchall()
    if len(res) == 0: # Kjører "kaffedb.sql" hvis applikasjonen ikke har blitt kjørt før
        db.run_script("kaffedb.sql")
    gui = GUI(db)
    lp = login.LoginPage(db, root, gui)
    lp.loginpage()
    root.mainloop()
    db.close()


if __name__ == '__main__':
    main()
