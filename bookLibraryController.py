# ======== REALIZAREA LEGATURII LOGICA - GUI ========


# Biblioteci pentru ferestre de tip eroare, incarcarea/afisarea imaginilor si verificarea existentei fisierelor
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class BookLibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.photo = None

        # ----- BIND BUTTONS (legam butoanele de functii) -----
        self.view.add_btn.config(command=self.addBook)
        self.view.edit_btn.config(command=self.editBook)
        self.view.delete_btn.config(command=self.deleteBook)

        self.view.sort_title_btn.config(
            command=lambda: self.sortBooks("title")
        )
        self.view.sort_author_btn.config(
            command=lambda: self.sortBooks("author")
        )
        self.view.sort_year_btn.config(
            command=lambda: self.sortBooks("year")
        )

        # Daca apesi pe o carte din lista, va completa datele din formular si va afisa coperta
        self.view.listbox.bind("<<ListboxSelect>>", self.fillEntries)

        # La fiecare introducere a unui caracter, se apeleaza searchBooks
        self.view.search_entry.bind("<KeyRelease>", self.searchBooks)

        self.refreshList()
        self.clearCover()

    # ----- HELPERS -----

    # Reactualizeaza lista (adica se vor sterge elementele din listbox si se vor reafisa)
    def refreshList(self, books=None):
        self.view.listbox.delete(0, "end")
        books = books if books is not None else self.model.books

        for book in books:
            self.view.listbox.insert(
                "end",
                f"{book['title']} | {book['author']} | {book['year']}"
            )

    # Goleste toate campurile de input din formular
    def clearEntries(self):
        for entry in (
            self.view.title_entry,
            self.view.author_entry,
            self.view.year_entry,
            self.view.image_entry
        ):
            entry.delete(0, "end")

    # Sterge imaginea copertii si se afiseaza textul "Coperta cartii"
    def clearCover(self):
        self.view.cover_canvas.delete("all")
        self.view.cover_canvas.create_text(
            self.view.cover_width // 2,
            self.view.cover_height // 2,
            text="Coperta cartii"
        )

    # ----- ACTIONS -----

    # Adaugare carte
    def addBook(self):
        try:
            self.model.addBook(
                self.view.title_entry.get().strip(),
                self.view.author_entry.get().strip(),
                self.view.year_entry.get().strip(),
                self.view.image_entry.get().strip()
            )
            self.refreshList()
            self.clearEntries()
            self.clearCover()
        except ValueError as e:
            messagebox.showerror("Eroare!", str(e))

    # Editare carte
    def editBook(self):
        try:
            index = self.view.listbox.curselection()[0]
            self.model.editBook(
                index,
                self.view.title_entry.get().strip(),
                self.view.author_entry.get().strip(),
                self.view.year_entry.get().strip(),
                self.view.image_entry.get().strip()
            )
            self.refreshList()
        except (IndexError, ValueError) as e:
            messagebox.showerror("Eroare!", str(e))

    # Stergere carte
    def deleteBook(self):
        try:
            index = self.view.listbox.curselection()[0]
            self.model.deleteBook(index)
            self.refreshList()
            self.clearEntries()
            self.clearCover()
        except IndexError:
            messagebox.showwarning("Atentie!", "Selecteaza o carte!")

    # Sortare carti
    def sortBooks(self, key):
        self.model.sortBooks(key)
        self.refreshList()

    # Cautare carte
    def searchBooks(self, event=None):
        query = self.view.search_entry.get().strip()
        results = self.model.searchBooks(query)
        self.refreshList(results)

    # Completeaza campurile de input cu valorile respective de la cartea selectata de utilizator
    def fillEntries(self, event):
        try:
            index = self.view.listbox.curselection()[0]
            displayedText = self.view.listbox.get(index)

            # Separam textul dupa separatorul "|"
            title = displayedText.split(" | ")[0]
            book = next(
                b for b in self.model.books if b["title"] == title
            )

            # Stergem valorile initiale din campurile de input si dupa introducem valorile noi
            self.clearEntries()
            self.view.title_entry.insert(0, book["title"])
            self.view.author_entry.insert(0, book["author"])
            self.view.year_entry.insert(0, book["year"])
            self.view.image_entry.insert(0, book["image"])

            self.showImage(book["image"])
        except (IndexError, StopIteration):
            pass

    # Afiseaza coperta cartii
    def showImage(self, image_name):
        self.view.cover_canvas.delete("all")

        # Daca nu exista nume de fisier, ne va afisa in frame 3 textul standard "Coperta cartii"
        if not image_name:
            self.clearCover()
            return

        # Construim calea completa catre imagine
        path = os.path.join("images", image_name)
        # Daca nu exista imagine, ne va afisa in frame 3 textul standard "Coperta cartii"
        if not os.path.exists(path):
            self.clearCover()
            return

        img = Image.open(path)

        # Cream un obiect PhotoImage, care poate fi folosit de Tkinter
        self.photo = ImageTk.PhotoImage(img)

        # Afisarea imaginii
        self.view.cover_canvas.create_image(
            self.view.cover_width // 2,
            self.view.cover_height // 2,
            image=self.photo
        )
