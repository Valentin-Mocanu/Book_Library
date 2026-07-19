# ======== CONTROLLER (LOGIC + GUI) ========


from tkinter import messagebox
from PIL import Image, ImageTk
import os


class BookLibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.photo = None

        # Bind buttons
        self.view.add_button.config(command=self.add_book)
        self.view.edit_button.config(command=self.edit_book)
        self.view.delete_button.config(command=self.delete_book)

        self.view.sort_title_button.config(
            command=lambda: self.sort_books("title")
        )
        self.view.sort_author_button.config(
            command=lambda: self.sort_books("author")
        )
        self.view.sort_year_button.config(
            command=lambda: self.sort_books("year")
        )

        # When you select a book from the list, the text fields will be automatically filled and the book cover will be displayed
        self.view.book_listbox.bind("<<ListboxSelect>>", self.fill_entries)

        # The search_books() method is called each time a character is typed
        self.view.search_entry.bind("<KeyRelease>", self.search_books)

        self.refresh_list()
        self.clear_book_cover()


    def add_book(self):
        try:
            self.model.add_book(
                self.view.title_entry.get().strip(),
                self.view.author_entry.get().strip(),
                self.view.year_entry.get().strip(),
                self.view.book_cover_entry.get().strip()
            )
            self.refresh_list()
            self.clear_entries()
            self.clear_book_cover()
        except ValueError as e:
            messagebox.showerror("Error!", str(e))


    def edit_book(self):
        try:
            index = self.view.book_listbox.curselection()[0]
            self.model.edit_book(
                index,
                self.view.title_entry.get().strip(),
                self.view.author_entry.get().strip(),
                self.view.year_entry.get().strip(),
                self.view.book_cover_entry.get().strip()
            )
            self.refresh_list()
        except (IndexError, ValueError) as e:
            messagebox.showerror("Error!", str(e))


    def delete_book(self):
        try:
            index = self.view.book_listbox.curselection()[0]
            self.model.delete_book(index)
            self.refresh_list()
            self.clear_entries()
            self.clear_book_cover()
        except IndexError:
            messagebox.showwarning("Warning!", "Please select a book!")


    def sort_books(self, key):
        self.model.sort_books(key)
        self.refresh_list()


    def search_books(self, event=None):
        query = self.view.search_entry.get().strip()
        results = self.model.search_books(query)
        self.refresh_list(results)


    def show_book_cover(self, image_name):
        self.view.cover_canvas.delete("all")

        # If image_name is empty, the "Book Cover" text will be shown in the third frame
        if not image_name:
            self.clear_book_cover()
            return

        path = os.path.join("images", image_name)
        # If the book cover does not exist, the "Book Cover" text will be shown in the third frame
        if not os.path.exists(path):
            self.clear_book_cover()
            return

        img = Image.open(path)

        self.photo = ImageTk.PhotoImage(img)

        self.view.cover_canvas.create_image(
            self.view.cover_width // 2,
            self.view.cover_height // 2,
            image=self.photo
        )


    def clear_book_cover(self):
        self.view.cover_canvas.delete("all")
        self.view.cover_canvas.create_text(
            self.view.cover_width // 2,
            self.view.cover_height // 2,
            font=("Arial", 20),
            fill="gray",
            text="Book Cover"
        )


    # -------------------------
    # REFRESH BOOK LIST
    # -------------------------
    def refresh_list(self, books=None):
        self.view.book_listbox.delete(0, "end")
        books = books if books is not None else self.model.books

        for book in books:
            self.view.book_listbox.insert(
                "end",
                f"{book['title']} | {book['author']} | {book['year']}"
            )


    # -------------------------
    # CLEAR ALL TEXT FIELDS
    # -------------------------
    def clear_entries(self):
        for entry in (
            self.view.title_entry,
            self.view.author_entry,
            self.view.year_entry,
            self.view.book_cover_entry
        ):
            entry.delete(0, "end")


    # -------------------------
    # FILL ALL TEXT FIELDS WITH THE SELECTED BOOK INFORMATION
    # -------------------------
    def fill_entries(self, event):
        try:
            index = self.view.book_listbox.curselection()[0]
            displayed_text = self.view.book_listbox.get(index)

            # Split the text using the " | " separator
            title = displayed_text.split(" | ")[0]
            book = next(
                b for b in self.model.books if b["title"] == title
            )

            # Delete the previous data from the text fields and add the new one
            self.clear_entries()
            self.view.title_entry.insert(0, book["title"])
            self.view.author_entry.insert(0, book["author"])
            self.view.year_entry.insert(0, book["year"])
            self.view.book_cover_entry.insert(0, book["image"])

            self.show_book_cover(book["image"])
        except (IndexError, StopIteration):
            pass