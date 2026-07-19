# ======== MAIN FILE ========

import tkinter as tk

from model import BookLibraryModel
from view import BookLibraryView
from controller import BookLibraryController


def main():
    root = tk.Tk()

    model = BookLibraryModel("books.csv")
    view = BookLibraryView(root)

    controller = BookLibraryController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()