# ======== INTERFATA GRAFICA (GUI) ========


# Biblioteca standard Python pentru GUI
import tkinter as tk


class BookLibraryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library")

        # Dimensiunea ferestrei
        self.root.geometry("900x450")
        # Culoarea fundalului
        root.configure(bg="#2c3e50")

        # ----- FRAME-URI -----
        self.left_frame = tk.Frame(root)
        self.center_frame = tk.Frame(root)
        self.right_frame = tk.Frame(root)

        # Pozitionarea frame-urilor pe grid
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)
        self.center_frame.grid(row=0, column=1, padx=10, pady=10)
        self.right_frame.grid(row=0, column=2, padx=10, pady=10)

        # ----- INPUT UTILIZATOR (FRAME 1)-----

        # Labels (text afisat in fereastra)
        tk.Label(self.left_frame, text="Titlul:").grid(row=0, column=0, sticky="w")
        tk.Label(self.left_frame, text="Autorul:").grid(row=1, column=0, sticky="w")
        tk.Label(self.left_frame, text="Anul:").grid(row=2, column=0, sticky="w")
        tk.Label(self.left_frame, text="Coperta:").grid(row=3, column=0, sticky="w")

        # Casute de inserare input carte
        self.title_entry = tk.Entry(self.left_frame, width=25)
        self.author_entry = tk.Entry(self.left_frame, width=25)
        self.year_entry = tk.Entry(self.left_frame, width=25)
        self.image_entry = tk.Entry(self.left_frame, width=25)

        # Pozitionarea casutelor pe grid
        self.title_entry.grid(row=0, column=0, columnspan=2, pady=2)
        self.author_entry.grid(row=1, column=0, columnspan=2, pady=2)
        self.year_entry.grid(row=2, column=0, columnspan=2, pady=2)
        self.image_entry.grid(row=3, column=0, columnspan=2, pady=2)

        # Label folosit ca spatiere intre elementele respective
        tk.Label(self.left_frame, text="", height=3).grid(row=4)

        # Textbox pentru cautarea unei carti
        tk.Label(self.left_frame, text="Cauta:").grid(row=5, column=0, sticky="w")
        self.search_entry = tk.Entry(self.left_frame, width=25)
        self.search_entry.grid(row=5, column=0, columnspan=2, pady=5)

        # Label folosit ca spatiere intre elementele respective
        tk.Label(self.left_frame, text="", height=3).grid(row=6)

        # ----- BUTOANE -----
        self.add_btn = tk.Button(self.left_frame, text="Adauga cartea", width=12)
        self.edit_btn = tk.Button(self.left_frame, text="Editeaza cartea", width=12)
        self.delete_btn = tk.Button(self.left_frame, text="Sterge cartea", width=12)

        self.add_btn.grid(row=7, column=0, pady=5)
        self.edit_btn.grid(row=7, column=1, pady=5)
        self.delete_btn.grid(row=8, column=0, columnspan=2, pady=5)

        self.sort_title_btn = tk.Button(self.left_frame, text="Sorteaza dupa titlu", width=18)
        self.sort_author_btn = tk.Button(self.left_frame, text="Sorteaza dupa autor", width=18)
        self.sort_year_btn = tk.Button(self.left_frame, text="Sorteaza dupa an", width=18)

        # Label folosit ca spatiere intre elementele respective
        tk.Label(self.left_frame, text="", height=3).grid(row=9)

        self.sort_title_btn.grid(row=10, column=0, pady=2)
        self.sort_author_btn.grid(row=10, column=1, pady=2)
        self.sort_year_btn.grid(row=11, column=0, columnspan=2, pady=2)

        # ----- LISTA CU CARTI (FRAME 2) -----
        self.listbox = tk.Listbox(self.center_frame, width=50, height=18)
        self.listbox.pack()

        # ----- COPERTA CARTII (FRAME 3) -----
        self.cover_width = 260
        self.cover_height = 400

        # Zona de desen pentru coperta
        self.cover_canvas = tk.Canvas(
            self.right_frame,
            width=self.cover_width,
            height=self.cover_height,
            bg="white",
            highlightthickness=2,
            highlightbackground="black"
        )
        self.cover_canvas.pack()
