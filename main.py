import tkinter as tk
from PIL import Image, ImageTk
import os


class IDARADZ:

    def __init__(self, root):

        self.root = root

        self.root.title("IDARA DZ")

        self.root.geometry("1400x850")

        self.root.configure(bg="#f5f5f5")

        self.root.minsize(1200, 750)

        self.assets = "assets"

        self.build_ui()

    def load_icon(self, filename, size):

        path = os.path.join(self.assets, filename)

        image = Image.open(path)

        image = image.resize(size)

        return ImageTk.PhotoImage(image)

    def build_ui(self):

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = tk.Frame(
            self.root,
            bg="#ffffff",
            width=150
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # HOME BUTTON

        self.home_icon = self.load_icon(
            "home.png",
            (40, 40)
        )

        self.home_btn = tk.Button(
            self.sidebar,
            image=self.home_icon,
            text="الرئيسية",
            compound="top",
            bg="black",
            fg="white",
            activebackground="black",
            activeforeground="white",
            relief="flat",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            width=100,
            height=80
        )

        self.home_btn.pack(
            pady=(30, 0)
        )

        # BOTTOM ICONS

        self.bottom_frame = tk.Frame(
            self.sidebar,
            bg="white"
        )

        self.bottom_frame.pack(
            side="bottom",
            pady=30
        )

        self.settings_icon = self.load_icon(
            "settings.png",
            (42, 42)
        )

        self.moon_icon = self.load_icon(
            "moon.png",
            (42, 42)
        )

        self.info_icon = self.load_icon(
            "info.png",
            (42, 42)
        )

        self.back_icon = self.load_icon(
            "back.png",
            (42, 42)
        )

        def create_side_icon(icon):

            btn = tk.Button(
                self.bottom_frame,
                image=icon,
                bg="white",
                relief="flat",
                cursor="hand2",
                activebackground="white",
                bd=0
            )

            btn.pack(
                pady=8
            )

            return btn

        self.settings_btn = create_side_icon(
            self.settings_icon
        )

        self.moon_btn = create_side_icon(
            self.moon_icon
        )

        self.info_btn = create_side_icon(
            self.info_icon
        )

        # LINE

        self.line = tk.Frame(
            self.bottom_frame,
            bg="black",
            height=3,
            width=70
        )

        self.line.pack(
            pady=12
        )

        self.back_btn = create_side_icon(
            self.back_icon
        )

        # =========================
        # MAIN AREA
        # =========================

        self.main = tk.Frame(
            self.root,
            bg="#f5f5f5"
        )

        self.main.pack(
            side="left",
            expand=True,
            fill="both"
        )

        # LOGO

        self.logo_img = self.load_icon(
            "logo.png",
            (520, 170)
        )

        self.logo_label = tk.Label(
            self.main,
            image=self.logo_img,
            bg="#f5f5f5"
        )

        self.logo_label.pack(
            pady=(70, 40)
        )

        # =========================
        # CARDS
        # =========================

        self.cards_frame = tk.Frame(
            self.main,
            bg="#f5f5f5"
        )

        self.cards_frame.pack()

        self.document_icon = self.load_icon(
            "document.png",
            (90, 90)
        )

        self.web_icon = self.load_icon(
            "web.png",
            (90, 90)
        )

        self.archive_icon = self.load_icon(
            "archive.png",
            (90, 90)
        )

        self.create_card(
            self.cards_frame,
            self.document_icon,
            "وثائق",
            "إنشاء وتعديل مختلف الوثائق\nالإدارية بسهولة",
            0
        )

        self.create_card(
            self.cards_frame,
            self.web_icon,
            "خدمات الكترونية",
            "الوصول إلى الخدمات الإلكترونية\nوالمنصات الرسمية",
            1
        )

        self.create_card(
            self.cards_frame,
            self.archive_icon,
            "ارشيف",
            "إدارة وأرشفة الملفات والوثائق\nوالوصول إليها بسهولة",
            2
        )

    def create_card(
        self,
        parent,
        icon,
        title,
        text,
        column
    ):

        card = tk.Frame(
            parent,
            bg="white",
            width=350,
            height=410,
            highlightbackground="#dddddd",
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=column,
            padx=25
        )

        card.grid_propagate(False)

        icon_label = tk.Label(
            card,
            image=icon,
            bg="white"
        )

        icon_label.pack(
            pady=(55, 25)
        )

        title_label = tk.Label(
            card,
            text=title,
            bg="white",
            fg="black",
            font=("Arial", 22, "bold")
        )

        title_label.pack()

        text_label = tk.Label(
            card,
            text=text,
            bg="white",
            fg="#666666",
            font=("Arial", 14),
            justify="center"
        )

        text_label.pack(
            pady=18
        )


root = tk.Tk()

app = IDARADZ(root)

root.mainloop()
