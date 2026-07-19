# ======== VIEW (GUI) ========


import tkinter as tk


class BookLibraryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library")

        self.root.geometry("900x460")
        root.configure(bg="#704848")

        # Frames
        self.left_frame = tk.Frame(root,
                                   bg="#E6E6E6",
                                   highlightthickness=2,
                                   highlightbackground="black")
        self.center_frame = tk.Frame(root,
                                     bg="#E6E6E6",
                                     highlightthickness=2,
                                     highlightbackground="black")
        self.right_frame = tk.Frame(root,
                                    bg="#E6E6E6",
                                    highlightthickness=2,
                                    highlightbackground="black")

        self.left_frame.grid(row=0, column=0, padx=(20, 0), pady=20)
        self.center_frame.grid(row=0, column=1, padx=20, pady=20)
        self.right_frame.grid(row=0, column=2, padx=(0, 20), pady=20)


        # -------------------------
        # FIRST FRAME - USER INPUT
        # -------------------------

        tk.Label(self.left_frame, text="Title:", bg="#E6E6E6").grid(row=0, column=0, pady=(10, 0), padx=(6,0), sticky="w")
        tk.Label(self.left_frame, text="Author:", bg="#E6E6E6").grid(row=1, column=0, padx=(6,0), sticky="w")
        tk.Label(self.left_frame, text="Year:", bg="#E6E6E6").grid(row=2, column=0, padx=(6,0), sticky="w")
        tk.Label(self.left_frame, text="Book cover:", bg="#E6E6E6").grid(row=3, column=0, padx=(6,0), sticky="w")

        self.title_entry = tk.Entry(self.left_frame, width=20)
        self.author_entry = tk.Entry(self.left_frame, width=20)
        self.year_entry = tk.Entry(self.left_frame, width=20)
        self.book_cover_entry = tk.Entry(self.left_frame, width=20)

        self.title_entry.grid(row=0, column=1, pady=(10, 2), padx=2)
        self.author_entry.grid(row=1, column=1, pady=2, padx=2)
        self.year_entry.grid(row=2, column=1, pady=2, padx=2)
        self.book_cover_entry.grid(row=3, column=1, pady=2, padx=2)

        # Spacing between GUI elements
        tk.Label(self.left_frame, text="", bg="#E6E6E6", height=3).grid(row=4)

        tk.Label(self.left_frame, text="Search:", bg="#E6E6E6").grid(row=5, column=0, padx=(6,0), sticky="w")
        self.search_entry = tk.Entry(self.left_frame, width=20)
        self.search_entry.grid(row=5, column=1, columnspan=2, pady=5, padx=2)

        tk.Label(self.left_frame, text="", bg="#E6E6E6", height=3).grid(row=6)

        self.add_button = tk.Button(self.left_frame,
                                    text="Add book",
                                    bg="#59CC5D",
                                    activebackground="#4EB352",
                                    width=12)
        self.edit_button = tk.Button(self.left_frame,
                                     text="Edit book",
                                     bg="#47ABFA",
                                     activebackground="#4099E0",
                                     width=12)
        self.delete_button = tk.Button(self.left_frame,
                                       text="Delete book",
                                       bg="#f44336",
                                       activebackground="#DB3C31",
                                       width=12)

        self.add_button.grid(row=7, column=0, pady=5)
        self.edit_button.grid(row=7, column=1, pady=5)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.sort_title_button = tk.Button(self.left_frame,
                                           text="Sort by title",
                                           bg="#C2C2C2",
                                           activebackground="#A8A8A8",
                                           width=12)
        self.sort_author_button = tk.Button(self.left_frame,
                                            text="Sort by author",
                                            bg="#C2C2C2",
                                            activebackground="#A8A8A8",
                                            width=12)
        self.sort_year_button = tk.Button(self.left_frame,
                                          text="Sort by year",
                                          bg="#C2C2C2",
                                          activebackground="#A8A8A8",
                                          width=12)

        tk.Label(self.left_frame, text="", bg="#E6E6E6", height=3).grid(row=9)

        self.sort_title_button.grid(row=10, column=0, pady=2)
        self.sort_author_button.grid(row=10, column=1, pady=2)
        self.sort_year_button.grid(row=11, column=0, columnspan=2, pady=(2, 10))


        # -------------------------
        # SECOND FRAME - BOOK LIST
        # -------------------------
        self.label_booklist = tk.Label(self.center_frame,
                                       text="Book list:",
                                       font=("Arial", 11, "bold", "underline"),
                                       bg="#E6E6E6")
        self.label_booklist.grid(row=0, column=0, sticky="w", pady=(6, 12), padx=(14, 0))
        self.book_listbox = tk.Listbox(self.center_frame, width=50, height=18, bg="#E6E6E6")
        self.book_listbox.grid(row=1, column=0)


        # -------------------------
        # THIRD FRAME - BOOK COVER
        # -------------------------
        self.cover_width = 260
        self.cover_height = 400

        # Display area for book cover
        self.cover_canvas = tk.Canvas(
            self.right_frame,
            width=self.cover_width,
            height=self.cover_height,
            bg="#E6E6E6"
        )
        self.cover_canvas.pack()
