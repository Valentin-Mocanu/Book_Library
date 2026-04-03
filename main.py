# ======== FISIERUL PRINCIPAL - PENTRU RULAREA APLICATIEI ========

# Biblioteca standard Python pentru GUI
import tkinter as tk

from bookLibraryModel import BookLibraryModel
from bookLibraryView import BookLibraryView
from bookLibraryController import BookLibraryController


def main():
    # Cream fereastra aplicatiei
    root = tk.Tk()

    # Cream obiectul care citeste datele din fisierul CSV si le valideaza
    model = BookLibraryModel("books.csv")

    # Cream interfata grafica (GUI)
    view = BookLibraryView(root)

    # Aici se realizeaza legatura dintre logica, datele din fisierul CSV si interfata grafica
    controller = BookLibraryController(model, view)

    # Bucla infinita ca sa nu se inchida fereastra
    root.mainloop()

if __name__ == "__main__":
    main()
