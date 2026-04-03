# ======== GESTIONAREA DATELOR ========


# Biblioteci pentru fisiere CSV, verificarea existentei fisierelor si anul curent
import csv
import os
from datetime import datetime


class BookLibraryModel:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.loadFromCSV()

    # ----- VALIDAREA CARTILOR -----
    def validateBook(self, title, author, year, image, editIndex=None):
        if not title or not author or not year:
            raise ValueError("Toate campurile sunt obligatorii!")

        if not year.isdigit():
            raise ValueError("Anul trebuie sa contina doar cifre!")

        # Facem convertirea din string in int si luam anul curent
        year = int(year)
        currentYear = datetime.now().year

        if year < 1000 or year > currentYear:
            raise ValueError("An invalid! Va rugam introduceti un an valid!")

        # Verificam daca exista o carte cu acelasi nume
        for i, book in enumerate(self.books):
            if book["title"].lower() == title.lower():
                if editIndex is None or i != editIndex:
                    raise ValueError("Exista deja o carte cu acest titlu!")

        return year

    # ----- ADAUGAREA CARTILOR -----
    def addBook(self, title, author, year, image):
        year = self.validateBook(title, author, year, image)

        # Folosim un dictionar pentru a stoca cartea temporar
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "image": image
        })
        # Salvam cartea in fisierul CSV
        self.saveToCSV()

    # ----- EDITAREA CARTILOR -----
    def editBook(self, index, title, author, year, image):
        year = self.validateBook(title, author, year, image, index)

        # Inlocuim cartea selectata
        self.books[index] = {
            "title": title,
            "author": author,
            "year": year,
            "image": image
        }
        self.saveToCSV()

    # ----- STERGEREA CARTILOR -----
    def deleteBook(self, index):
        self.books.pop(index)
        self.saveToCSV()

    # ----- SORTAREA CARTILOR -----
    def sortBooks(self, key):
        if key == "year":
            self.books.sort(key=lambda x: int(x[key]))
        else:
            self.books.sort(key=lambda x: x[key].lower())

    # ----- INCARCAREA DATELOR DIN FISIERUL CSV -----
    def loadFromCSV(self):
        # Conditie pusa ca in momentul in care nu exista fisierul, sa nu crape aplicatia
        if not os.path.exists(self.filename):
            return

        with open(self.filename, newline="", encoding="utf-8") as f:
            # Citim randurile ca pe niste dictionare
            reader = csv.DictReader(f)
            self.books = []

            for row in reader:
                row["year"] = int(row["year"])  # Conversie din string in int
                self.books.append(row)

    # ----- SALVAREA DATELOR IN FISIERUL CSV -----
    def saveToCSV(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["title", "author", "year", "image"]
            )
            writer.writeheader()
            writer.writerows(self.books)

    # ----- CAUTAREA CARTILOR -----
    def searchBooks(self, query):
        query = query.lower().strip()
        if not query:
            return self.books

        return [
            book for book in self.books
            if query in book["title"].lower()
               or query in book["author"].lower()
        ]
