# ======== MODEL (LOGIC) ========


import csv
import os
from datetime import datetime


class BookLibraryModel:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_from_csv()

    # -------------------------
    # VALIDATE BOOK
    # -------------------------
    def validate_book(self, title, author, year, image, edit_index=None):
        if not title or not author or not year:
            raise ValueError("All fields are required!")

        if not year.isdigit():
            raise ValueError("The year must contain only digits!")

        year = int(year)
        current_year = datetime.now().year

        if year < 1000 or year > current_year:
            raise ValueError("Invalid year! Please enter a valid year!")

        # Check if a book with the same year exists
        for i, book in enumerate(self.books):
            if book["title"].lower() == title.lower():
                if edit_index is None or i != edit_index:
                    raise ValueError("A book with the same year already exists!")

        return year


    # -------------------------
    # ADD BOOK
    # -------------------------
    def add_book(self, title, author, year, image):
        year = self.validate_book(title, author, year, image)

        # We use a dictionary to temporarily store the book
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "image": image
        })
        self.save_to_csv()


    # -------------------------
    # EDIT BOOK
    # -------------------------
    def edit_book(self, index, title, author, year, image):
        year = self.validate_book(title, author, year, image, index)

        # Replace selected book
        self.books[index] = {
            "title": title,
            "author": author,
            "year": year,
            "image": image
        }
        self.save_to_csv()


    # -------------------------
    # DELETE BOOK
    # -------------------------
    def delete_book(self, index):
        self.books.pop(index)
        self.save_to_csv()


    # -------------------------
    # SORT BOOKS
    # -------------------------
    def sort_books(self, key):
        if key == "year":
            self.books.sort(key=lambda x: int(x[key]))
        else:
            self.books.sort(key=lambda x: x[key].lower())


    # -------------------------
    # LOAD BOOKS FROM CSV FILE
    # -------------------------
    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, newline="", encoding="utf-8") as f:
            # Read the rows as dictionaries
            reader = csv.DictReader(f)
            self.books = []

            for row in reader:
                row["year"] = int(row["year"])  # string to int conversion
                self.books.append(row)


    # -------------------------
    # SAVE BOOKS TO CSV FILE
    # -------------------------
    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["title", "author", "year", "image"]
            )
            writer.writeheader()
            writer.writerows(self.books)


    # -------------------------
    # SEARCH BOOKS
    # -------------------------
    def search_books(self, query):
        query = query.lower().strip()
        if not query:
            return self.books

        return [
            book for book in self.books
            if query in book["title"].lower()
               or query in book["author"].lower()
        ]
